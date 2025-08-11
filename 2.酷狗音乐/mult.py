'''
批量采集需要核心流程
1、对比生成两个歌曲播放链接的请求参数
2、找到两个请求参数的不同部分
3、逆向寻找不同部分生成的过程
4、模拟生成对应的参数
'''

import os
import hashlib
import requests
import re
import time
import json
from tqdm import tqdm

# 设置环境目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

headers = {
  'content-type':'application/x-www-form-urlencoded',
  'cookie':'NMTID=00Ol8woFUCX2kcw0EdIkQNR8-Cq0LoAAAGVxsBc0Q; _ntes_nnid=d1d2b843473620b40d20ab64bae0a898,1742796253420; _ntes_nuid=d1d2b843473620b40d20ab64bae0a898; WEVNSM=1.0.0; WNMCID=uqnekl.1742796255073.01.0; WM_TID=QI4kA7oyeidBBRQEBUPGJ7BotRU%2B%2FXPF; __snaker__id=D6swI3DkieIBRmMd; sDeviceId=YD-96li8m9pvWhEVlAAUVLSN%2FV8oVDBRulN; ntes_utid=tid._.GFHUSZdE9R9ER1REAAOTJrB84QDBB4Pm._.0; __remember_me=true; ntes_kaola_ad=1; P_INFO=13628108279|1747731894|1|music|00&99|null&null&null#hub&420100#10#0|&0||13628108279; _iuqxldmzr_=32; __csrf=d4c42c8435aba96d5191a83f6345aaaa; JSESSIONID-WYYY=0JZDf8s5xAi2n0%2Br%2BOxXw8KqB7A7bI5fCM%2BO2d%2FIVBP%5CN2IvQ3h6SxZBzV%2BxKXvtFX5Pm2V5RelrV1f7oJaa4cywo7Kqf9oxBN%2BOPx3rqS7AsRzpDkoFX4Z28B0KCNo4mmmn3fpEz%2FJ9NNFEASf%5CTWfFXbV522MiqThhdT%2F4EJ%2B1I8i3%3A1752548935928; WM_NI=g%2BcPNu8QArQO7auHh%2FsLAOEj8aEAy40xMYLlMc7dVnin44lkhk1OIn%2BWQwmrZVal3dnSUAAWv6GVRKpQ22XuBF0baMaEc5vlxrl%2FI3h%2FwPdOEYoWJic6J9IKZoHJEExFY0Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee85c27ea6998487c44486a88fa2d14f938e8a83d23b869daa96b4808ab38b82ea2af0fea7c3b92aa5f5adb1cd7ffc8f8f93d445f5bfbba9eb25b1948fb0c862fcbf8ba2fc40f4a883bacf688fbdf985d566abb2fcd5ef61acb5ffb0cc66e9899f98f07a9a8aaf8db270ae8d9ba2c45db6ea89b7d141b48ffed3db7f829a0083e447a39badd6f568bcaea4d0cc39acf1b9b1e7458787a1b8c963a1ea86dacc419ab188abc84fbc9a97d1d437e2a3; gdxidpyhxdE=AGj%5Co2Z%2BuO3ZsGcuK70qiQXfe1qrodXnMLpcrahi8zJ88tKe6oUshzgvHNCXX5jINgqkZ%5C4L6RX2psJ6uaaXaBBRvfbpXXUZmBCdZbAs%2FjiJXddhxgGe%5C9eMp%5CgbGxBrRownQDSABcX871fR246B7mrZ8g3%2BV8k%2FeXBYb6KAfIvfpINN%3A1752548042674; MUSIC_U=0078BFD0D3F3AE1D32E973229EDB09CB578859D951C7945803DA4E80F4F7333BE49BD069FD8A71A3A5070D07AC0D14749A7AFC65289E71F5AF48BC7E6D229BC157B17F10959F3C07B19A1090DB341ADF50E72B4C187E51BAE0E7DB58F53732B27382750BDF39AA34D5972B3E3393F16007FE55F383C5650D49255F70AFA9983FFD2A3DA4B2C7D4D4AC9EAAA2E768AD8BAF054CAF36A4F797DBC507F499241C5D5283310A752D3F05141F779FF174A8267ECD4E25EEB2CFF1251ED60C5C6976096607EB525ADEB2A2C7C22762A9BFBAD54A8A5BE312D16E57209731E5D6369BEBC4A9619ED34B47437E43E42439B1FFAF87A5B7B4B63406B99A9871266628BF1F852A0FF72C168FE98BF756EBA8BC7C139DB6A964C0305863861A35A52FA03BE997932086BE44B97538E231A72DA819A8AFDB5E1E76505BDCB513B194D216947D7B89E0B176570D84CCEEA18C7CB8FE3615B1A21D63FF4F1910DADF3CDE34EB4B78; __csrf=6d3df568e8e2f8c00c0481b5a14fbabc; playerid=50301475',
  'referer':'https://music.163.com/', # 防盗链
  'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

# 创建文件夹目录
auto_dir = 'auto'
if not os.path.exists(auto_dir):
    os.makedirs(auto_dir)
    print(f'创建文件夹: {auto_dir}')

base_params = {
  'srcappid': '2919',
  'clientver': '20000',
  'mid': '42cf390e04a11d7234dcada6c7cd7f2c',
  'uuid': '42cf390e04a11d7234dcada6c7cd7f2c',
  'dfid': '4XRoeb23SODi1H7h7n0qhfH8',
  'appid': '1014',
  'platid': '4',
  'token': '9f37d7f8e9c78f2297e0afa9051cf48a380dd4acf78ed97b16b398735576b593',
  'userid': '702758808',
}

# 生成signature的方法(专辑id需要动态传入) 这里顺序非常重要，顺序会印象生成的结果
def get_signature(now_time, album_id):
    s = [
        'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt',
        'appid=1014',
        f'clienttime={now_time}',
        'clientver=20000',
        'dfid=4XRoeb23SODi1H7h7n0qhfH8',
        f'encode_album_audio_id={album_id}',
        'mid=42cf390e04a11d7234dcada6c7cd7f2c',
        'platid=4',
        'srcappid=2919',
        'token=9f37d7f8e9c78f2297e0afa9051cf48a380dd4acf78ed97b16b398735576b593',
        'userid=702758808',
        'uuid=42cf390e04a11d7234dcada6c7cd7f2c',
        'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    ]
    return hashlib.md5(''.join(s).encode('utf-8')).hexdigest()

def main():
  # 获取热歌榜列表
  top_songs_url = 'https://www.kugou.com/yy/html/rank.html'
  song_html = requests.get(top_songs_url, headers=headers).text
  # with open(os.path.join(auto_dir, 'top_songs.html'), 'w', encoding='utf-8') as f:  
  #     f.write(song_html)

  pattern = r'<li.*?title="(.*?)".*?data-eid="(.*?)".*?>'   

  result = re.findall(pattern, song_html)

  songs= []
  for item in result:
    title, eid = item
    # 从title中获取歌手和歌名
    singer, song_name = title.split(' - ')
    songs.append({
      'singer': singer,
      'song_name': song_name,
      'eid': eid
    })

  print(len(songs))

   # 循环下载歌曲
  for song in tqdm(songs):
    params = base_params.copy()
    now_time = int(time.time() * 1000)
    params['encode_album_audio_id'] = song['eid']
    params['signature'] = get_signature(now_time, song['eid'])
    params['clienttime'] = now_time
    response = requests.get('https://wwwapi.kugou.com/play/songinfo', params=params, headers=headers)
    data = response.json()

  #  执行下载
    play_url = data.get('data', {}).get('play_url', '')
    if play_url:
      response = requests.get(play_url, headers=headers)
      with open(os.path.join(auto_dir, f'{song["singer"]} - {song["song_name"]}.mp3'), 'wb') as f:
        f.write(response.content)
    else:
      print(f'{song["singer"]} - {song["song_name"]} 下载失败')



if __name__ == '__main__':
  main()