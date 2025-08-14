import requests
import os
from hashlib import md5
import re
import time

music_dir = os.path.join(os.path.dirname(__file__), 'music')

if not os.path.exists(music_dir):
  os.makedirs(music_dir)

'''
例子：邓紫棋的 唯一 
播放地址：https://webfs.kugou.com/202507151338/ac25adee66820aac785f9fe1548d55e8/v3/ab05b8f658851282dcb2cbad548aeb9b/yp/p_0_960139/ap1014_us702758808_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx590964610_s799589023.mp3
'''

'''模拟请求头'''
headers = {
  'content-type':'application/x-www-form-urlencoded',
  'cookie':'NMTID=00Ol8woFUCX2kcw0EdIkQNR8-Cq0LoAAAGVxsBc0Q; _ntes_nnid=d1d2b843473620b40d20ab64bae0a898,1742796253420; _ntes_nuid=d1d2b843473620b40d20ab64bae0a898; WEVNSM=1.0.0; WNMCID=uqnekl.1742796255073.01.0; WM_TID=QI4kA7oyeidBBRQEBUPGJ7BotRU%2B%2FXPF; __snaker__id=D6swI3DkieIBRmMd; sDeviceId=YD-96li8m9pvWhEVlAAUVLSN%2FV8oVDBRulN; ntes_utid=tid._.GFHUSZdE9R9ER1REAAOTJrB84QDBB4Pm._.0; __remember_me=true; ntes_kaola_ad=1; P_INFO=13628108279|1747731894|1|music|00&99|null&null&null#hub&420100#10#0|&0||13628108279; _iuqxldmzr_=32; __csrf=d4c42c8435aba96d5191a83f6345aaaa; JSESSIONID-WYYY=0JZDf8s5xAi2n0%2Br%2BOxXw8KqB7A7bI5fCM%2BO2d%2FIVBP%5CN2IvQ3h6SxZBzV%2BxKXvtFX5Pm2V5RelrV1f7oJaa4cywo7Kqf9oxBN%2BOPx3rqS7AsRzpDkoFX4Z28B0KCNo4mmmn3fpEz%2FJ9NNFEASf%5CTWfFXbV522MiqThhdT%2F4EJ%2B1I8i3%3A1752548935928; WM_NI=g%2BcPNu8QArQO7auHh%2FsLAOEj8aEAy40xMYLlMc7dVnin44lkhk1OIn%2BWQwmrZVal3dnSUAAWv6GVRKpQ22XuBF0baMaEc5vlxrl%2FI3h%2FwPdOEYoWJic6J9IKZoHJEExFY0Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee85c27ea6998487c44486a88fa2d14f938e8a83d23b869daa96b4808ab38b82ea2af0fea7c3b92aa5f5adb1cd7ffc8f8f93d445f5bfbba9eb25b1948fb0c862fcbf8ba2fc40f4a883bacf688fbdf985d566abb2fcd5ef61acb5ffb0cc66e9899f98f07a9a8aaf8db270ae8d9ba2c45db6ea89b7d141b48ffed3db7f829a0083e447a39badd6f568bcaea4d0cc39acf1b9b1e7458787a1b8c963a1ea86dacc419ab188abc84fbc9a97d1d437e2a3; gdxidpyhxdE=AGj%5Co2Z%2BuO3ZsGcuK70qiQXfe1qrodXnMLpcrahi8zJ88tKe6oUshzgvHNCXX5jINgqkZ%5C4L6RX2psJ6uaaXaBBRvfbpXXUZmBCdZbAs%2FjiJXddhxgGe%5C9eMp%5CgbGxBrRownQDSABcX871fR246B7mrZ8g3%2BV8k%2FeXBYb6KAfIvfpINN%3A1752548042674; MUSIC_U=0078BFD0D3F3AE1D32E973229EDB09CB578859D951C7945803DA4E80F4F7333BE49BD069FD8A71A3A5070D07AC0D14749A7AFC65289E71F5AF48BC7E6D229BC157B17F10959F3C07B19A1090DB341ADF50E72B4C187E51BAE0E7DB58F53732B27382750BDF39AA34D5972B3E3393F16007FE55F383C5650D49255F70AFA9983FFD2A3DA4B2C7D4D4AC9EAAA2E768AD8BAF054CAF36A4F797DBC507F499241C5D5283310A752D3F05141F779FF174A8267ECD4E25EEB2CFF1251ED60C5C6976096607EB525ADEB2A2C7C22762A9BFBAD54A8A5BE312D16E57209731E5D6369BEBC4A9619ED34B47437E43E42439B1FFAF87A5B7B4B63406B99A9871266628BF1F852A0FF72C168FE98BF756EBA8BC7C139DB6A964C0305863861A35A52FA03BE997932086BE44B97538E231A72DA819A8AFDB5E1E76505BDCB513B194D216947D7B89E0B176570D84CCEEA18C7CB8FE3615B1A21D63FF4F1910DADF3CDE34EB4B78; __csrf=6d3df568e8e2f8c00c0481b5a14fbabc; playerid=50301475',
  'referer':'https://music.163.com/', # 防盗链
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

def down_music(url:str, name:str):
  print(f'正在下载{name}...')
  content = requests.get(url, headers=headers).content
  with open(os.path.join(music_dir, f'{name}.mp3'), 'wb') as f:
    f.write(content)
  print(f'下载完成{name}')

def single_get_music_url():
  url = 'https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1752557930089&mid=42cf390e04a11d7234dcada6c7cd7f2c&uuid=42cf390e04a11d7234dcada6c7cd7f2c&dfid=4XRoeb23SODi1H7h7n0qhfH8&appid=1014&platid=4&encode_album_audio_id=9ruf7m3b&token=9f37d7f8e9c78f2297e0afa9051cf48ab448be2272bc85232b33e698bda72e40&userid=702758808&signature=0993dfba147d1895a8ddffb08b5e71bc'
  response = requests.get(url, headers=headers)
  json_data = response.json()
  play_url = json_data['data']['play_url']
  if play_url:
    down_music(play_url, '唯一')
  else:
    print('没有找到播放地址')

'''
批量采集数据对弈
邓紫棋：唯一
时代少年团：登顶 https://www.kugou.com/mixsong/crngtu80.html
images中对比两个数据请求的字段信息，存在3个字段不同
clienttime             > 当前请求的时间戳，自己构建就行
encode_album_audio_id  > 专辑id crngtu80  在dom中就能获取到
signature              > 签名，调试窗口搜索 signature 关键词，查看如何构建的过程，需要对比最终获取歌曲的字符是否一致，因为可能存在多个 signature 字符，debugger存在干扰性

调试后结论：signature 构建是是一个数组组成的字符串进行构建然后使用md5加密(为什么是md5，经验所谈)

[
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014", 
    "clienttime=1752563337741",
    "clientver=20000",
    "dfid=4XRoeb23SODi1H7h7n0qhfH8",
    "encode_album_audio_id=crngtu80",
    "mid=42cf390e04a11d7234dcada6c7cd7f2c",
    "platid=4",
    "srcappid=2919",
    "token=9f37d7f8e9c78f2297e0afa9051cf48ab448be2272bc85232b33e698bda72e40",
    "userid=702758808",
    "uuid=42cf390e04a11d7234dcada6c7cd7f2c",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]

对比数据，除了首尾两个字符串，中间的内容和images中的图片是一致的
'''

def get_signature(time:int, album_audio_id:str):
  s = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014", 
    f"clienttime={time}",
    "clientver=20000",
    "dfid=4XRoeb23SODi1H7h7n0qhfH8",
    f"encode_album_audio_id={album_audio_id}",
    "mid=42cf390e04a11d7234dcada6c7cd7f2c",
    "platid=4",
    "srcappid=2919",
    "token=9f37d7f8e9c78f2297e0afa9051cf48ab448be2272bc85232b33e698bda72e40",
    "userid=702758808",
    "uuid=42cf390e04a11d7234dcada6c7cd7f2c",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
  ]
  return md5(('').join(s).encode('utf-8')).hexdigest()


def batch_get_music_url():
  list_url = 'https://www.kugou.com/yy/html/rank.html'
  html = requests.get(list_url, headers=headers).text
  # 构建re获取<li class=" " title="时代少年团 - 登顶" data-index="0" data-eid="crngtu80"> 里面的 title和data-eid，忽略 data-index和class
  # pattern = re.compile(r'<li title="(.*?)" data-eid="(.*?)">')
  pattern = r'<li.*?title="(.*?)".*?data-eid="(.*?)"'
  matches = re.findall(pattern, html)
  for title, album_audio_id in matches:
    now_time = str(int(time.time() * 1000))
    # 构建url
    url = f'https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime={now_time}&mid=42cf390e04a11d7234dcada6c7cd7f2c&uuid=42cf390e04a11d7234dcada6c7cd7f2c&dfid=4XRoeb23SODi1H7h7n0qhfH8&appid=1014&platid=4&encode_album_audio_id={album_audio_id}&token=9f37d7f8e9c78f2297e0afa9051cf48ab448be2272bc85232b33e698bda72e40&userid=702758808&signature={get_signature(now_time, album_audio_id)}'
    song_info = requests.get(url, headers=headers).json()
    play_url = song_info['data']['play_url']
    down_music(play_url, title)





if __name__ == '__main__':
  # single_get_music_url()
  batch_get_music_url()