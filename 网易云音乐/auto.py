'''自动批量采集
1、核心：分析请求参数的变化规律
2、在free中，请求参数就2个，一个params，一个encSecKey
3、在search中，搜索encSecKey，找到可能符合条件的代码，打断点
4、参考images/1.png，可以断定只有JSON.stringify(e)的参数会跟随e改变，其他都是固定的
5、将js代码复制下来,在net.js中，核心方法是getSign，使用getSign时候会报错，根据报错缺什么补什么
6、真正播放的时候，JSON.stringify(e)中的e参考images/3.png
7、所以批量自动采集的基本思路就是获取到所有的id即可，然后使用getSign方法获取到params和encSecKey
8、然后使用requests.get(url = url, headers=headers, params=params, data=data)获取到音频资源
9、然后下载资源
'''

import requests
import re
import os
import execjs
from tqdm import tqdm

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 创建目录
auto_dir = 'auto'
if not os.path.exists(auto_dir):
  os.makedirs(auto_dir)


'''模拟请求头'''
headers = {
  'content-type':'application/x-www-form-urlencoded',
  'cookie':'NMTID=00Ol8woFUCX2kcw0EdIkQNR8-Cq0LoAAAGVxsBc0Q; _ntes_nnid=d1d2b843473620b40d20ab64bae0a898,1742796253420; _ntes_nuid=d1d2b843473620b40d20ab64bae0a898; WEVNSM=1.0.0; WNMCID=uqnekl.1742796255073.01.0; WM_TID=QI4kA7oyeidBBRQEBUPGJ7BotRU%2B%2FXPF; __snaker__id=D6swI3DkieIBRmMd; sDeviceId=YD-96li8m9pvWhEVlAAUVLSN%2FV8oVDBRulN; ntes_utid=tid._.GFHUSZdE9R9ER1REAAOTJrB84QDBB4Pm._.0; __remember_me=true; ntes_kaola_ad=1; P_INFO=13628108279|1747731894|1|music|00&99|null&null&null#hub&420100#10#0|&0||13628108279; _iuqxldmzr_=32; WM_NI=5iV0aMIQveCNxI0Y4qDozUcLNyFQdAB1fUX5uBG%2B5Rlvz10f4wwJa533clcjTJJq5yIvowZS40NvLekTJlqVHKpIiTu5gdGrnGE64KqNfUiG9lmrT1RU%2BTvxvSnk%2BptLWjc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb7e842a1b99796ea3c96e78eb2d14a838b9badd63c918f8a8bd780bbabbaa3bb2af0fea7c3b92af7b79ad1e4478b8fba86c246bc9700bab77b88b1b6b6e2488ea78ab2e74b82efaab6db3fb79e89ccb85ab0aab6d2b36ef8a9b9abe43ff1edad8de26298968692b8738baaa198d959f8f08297cf6fa98c868df45e8c95c0aaec60b7eba985c67aae998bd7b741b392aab6ec4dfbb4a393d73b928be5b5f574b68da28caa7cb894998be237e2a3; gdxidpyhxdE=9hI%2FZekUVfMk%5C4p5SNWzMizAtCQa2%2Fa5vAGKBMXjDeXhP%5CwdgmX4oD3qY3SJ2cxoRzAPVVYy2rIWCi1uQeEkO5YXsMu5BK3hP50Gcc2OjXNOVLQZMo30kPVPMQnib28QLKQ0zjS8HeJZmyBNjSeQtG90eUsNaRVwdB3gsILzncjUkxEp%3A1753432309115; __csrf=e2ce6e09654adb9bb077460f35cf65ee; MUSIC_U=009FB6A75E102E71BC86B8CFF70D446B52617E0F43CA2C86C416A7F24C5DAAFCB82EF72049735A700623F73ABE242598476218119777C9414718ED3B277E81D3DB093E5EF04D3F99A1F76CBAB97B9639FF3D189CB306E3D5A9232DF6F9B283B24C5733687AC7D985F540C5E775245009018A51CB197C5273B346EEA1D5F4A9F61FC6C1407DF2080E93CBC42432813C33608AD38F6CAB3EC8CB7CEA8B9C904D524D42E2B6EC9E8CB22772259758F99E8F42E9E0644EE20021C0ECC5F24BC4CEDC5EC34050AD4F5FD9015C01E4F45FC3ED4192B5557BBDD1CB1DE9AC2973FA79FB4ACC7333A1911A4094261905EEE76A298EB7FEC55C26A98105A739F1B25EE7ABA4DEC361F16036F55E8135B7919F250190FEA109FB3636A0FF242197BCE8FCD3B9291025259AD1417D4564512E30F4C858AAAEC4AC84C0ADB3F6A98C4717261778FE3FC5E4EED85656A531425F766A9EF2F4B8C6A37D150D280EC69401C9ACE2BE1726DAE24D33A06BAA08CCA24B674F99348D355122C202B40CDCCB1F0D8A327EDE74A29482BE365B3E7573C886ADE1E1AD4EC1B53B4FD31D18B8C45B0E0F0162; playerid=61395946; JSESSIONID-WYYY=TZedxiwllVlqCt9KpsVJJPrnPpm%5C4rUWeHP%2F4JfawrWAqW0%5C%5CpTpm9hkYmX%2B35wl%5C7WhgHtlc6PnUfjT4DybZUtl3Dw133hA%5CGsecCcDMjKfIWQ%2BadZ%5CwUDhxmkm4Nlb0bgTWUIstSQqXIvRb2ZABUxcsOufWVPFNf57PnXsp1yqkTVM%3A1753436639599',
  'referer':'https://music.163.com/discover/toplist?id=3778678', # 防盗链
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=e2ce6e09654adb9bb077460f35cf65ee'



'''以热歌榜为例
1、网址https://music.163.com/discover/toplist?id=3778678
2、从1返回的text中使用正则获取到所有的数据
'''
# 热歌榜的网址
hot_link = 'https://music.163.com/discover/toplist?id=3778678'

# 请求热歌榜
hot_list_text = requests.get(url = hot_link, headers=headers).text

with open('hot_list_text.html', 'w', encoding='utf-8') as f:
  f.write(hot_list_text)

# 使用正则获取到所有的数据
song_ids = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', hot_list_text)


for song_id, song_name in tqdm(song_ids):
  iox = {
      'ids': f'[{song_id}]',
      "level": "standard",
      "encodeType": "aac",
      "csrf_token": "d4c42c8435aba96d5191a83f6345aaaa"
    }
  # 循环id，调用js获取params和encSecKey
  with open('net.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    

  ctx = execjs.compile(js_code)
  params = ctx.call('getSign', iox)

  params, encSecKey = params['encText'], params['encSecKey']

  # 获取真实音乐资源地址
  music_url = requests.post(url = url, headers=headers, data={'params': params, 'encSecKey': encSecKey}).json()['data'][0]['url']

  # 执行下载
  

  # 下载资源
  with open(f'{auto_dir}/{song_name}.mp3', 'wb') as f:
    f.write(requests.get(url = music_url, headers=headers).content)