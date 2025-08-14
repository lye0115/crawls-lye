import requests
from hashlib import md5
import time

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
  'cookie':'lid=tb17200_45; cna=wCDAIDoHDE8CAXdgON7apJZN; wk_cookie2=1342e260925ef96ff8ee72fb444fc947; wk_unb=W8twr6MPjEz5; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zMG1aAN%2F1UrnbH18zE9KTygW11QdYfVQqHnGms3HovfhWHj7Pt29rPiQxxqoSW%2B0wxIUUmlSlkg4wQXEdQItWUxWI34xHMD6OAL%2BxDyrHBsXD%2Fp244pFOlnIv4XoffhN2u75T6VC5VsPxYKO6P3rtXP4WcqCFB070xb7RNwXRrGAip28mPZrTwzwtZInvj7oSHWAO94Uz1Z801yaxqeaOc45nB5%2FDBu9w01EeYXy2OoKgs6YmWwYXUydSywC4MjauvlqYO%2BU7fyLJ0HgUgrjtO2yt4ID1SmqMcSONLz3hapX%2BdBB9EvqicKty3s5zo90KxNoNiA21b0TySxIqIUq3NKHdh5ROpxNhs0Gaaa8Pd%2BuvDYnnXtyVbHBCDfADHU4HjJ4FtI8yeoyW1DJJRWM9pk9boweaazba%2B4w1hlZ4ZxE7AJtNerzw%2BJcsMa4bEKR2dv%2BZP7WR2CroZPIetETGhM3821zG6RpVlOzwe5kRvtIUTVLY5XyesZEQgskNN4eyA%2Ba03XM4UJV%2FyJTFk%2FjQQC8jWEVL7gEt4lXBvy0sLbq2g6IIds8wRjzAttb1EKsxIIduEqVpVz0vd20Hcfrh4qSVc%2FYPj99KXI7dLtdW5466cFmAotnDvCR6KhBCj4uIsjqHMi1wVSJCqb%2FEwnVCC9TMHbzFz7G6b4mXd4GcvXUaeBRSkmqQXnPJTaoSe2MyqRM5471njKRh8krEOGlTHP4WsIay4fmIUJ4spxfUf2ujaLycptYy0r1t49YKj8SoXuvSEqgd11VyOQn43NaKOVGmuJ%2BqCIFx3ggAvQKaL66fPnBljBeiHMi1sVGpVAEmnEDKCSlVCRMlMZtDclZBNR%2B0CpUJkZ9kIxRZxwe2MGU5%2FW4thWh4tWSsIIJAnWBaXwDvmYoGxnKsBBwN%2FQpd6%2BqWv7QHM72oQvYt%2BDPX00xJ0vCEpTf%2FqRFBmHbYi7JYKVJ0SnrFABv4TPy9rtO12y%2FQJ9OVxxIZVp%2BfXwmjzkhxtWeX4sc91HRKKaMMzPGowRfW4QOq0kMm9N04fQ9ukP1nDxv1eBVWl%2FG5k9zhpx1MRHXb0CayJFUzxtT%2BJC0nqR%2B50lymmih2XAc08RwQLq2nj; miid=118027507489245424; tkSid=1752566500612_556863009_0.0; _l_g_=Ug%3D%3D; lgc=tb17200_45; cookie3_bak=16c78766e7d5291b2c695da21313cf02; cookie1=W8zOT%2F%2FlhP%2FunSF5b2tj9M5fBqrRm9qW056DR5UFi%2BY%3D; login=true; cookie2=16c78766e7d5291b2c695da21313cf02; env_bak=FM%2BgmZzCKPPmPiNCG%2BcmEZpsWbj6fuTn%2B55U44uqbAfO; cancelledSubSites=empty; sg=548; sn=; _tb_token_=ee4e3eee5ee8e; dnk=tb17200_45; uc1=pas=0&cookie14=UoYbySQkOvRT8g%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=WqG3DMC9VAQiUQ%3D%3D; uc3=id2=W8twr6MPjEz5&vt3=F8dD2fpgw4HZzFCkssg%3D&nk2=F5REOWeEfJ%2BaPw%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=tb17200_45; havana_lgc_exp=1783670503724; uc4=id4=0%40WeiuNI76Yw2Pp4%2BDDvl0Ytu0lKg%3D&nk4=0%40FY4PawtB%2Bp3J0Ash0U884ltC9Bt6; unb=824502584; cookie17=W8twr6MPjEz5; _nk_=tb17200_45; sgcookie=E100IsR5mgy4rN4%2Bac16ZN8jw9wIE1BSx7qkGhmFXSE96KS9S6SX4R8j0FNKxD6Hs9ThycS5LpNLFJ1Awr%2FFV657PHzEUlOD8R5VXl%2FU325xGzgeQcL80cwvQ1sjP57a722d; t=c94dfb5772c487fee46a93792483dd09; csg=be517526; cookie3_bak_exp=1752825703721; havana_sdkSilent=1752726651651; xlly_s=1; isg=BO_vrp5e2xGnc9CKALyY10C0fgX5lEO21k1WgwF84t72UA5SCWbkBJ5I1kDuKBsu; bxuab=0; mtop_partitioned_detect=1; _m_h5_tk=67daeee6a1c7e590c815a617f83a87a0_1752664724280; _m_h5_tk_enc=c45439deade5b5d2da658c4476136e06; tfstk=gjUjHQ1F6RUyUy391mfyRc9ife315_7FcCGTt5L26q3x1FN3CSua6Azs582-Xru4g8__tJiqXPka5I47dF8VniV95VuOL97F8SxmSVBefoMn3KcK1EQZXVd-ofPjg9TR8SVDwI9OTuQe1de7ZxHTBmnJwjkJkKhTB0L-sYLx6Eh9e_MoeEptXfHJeXhBHnetW_N-EfG9MRnAN4Ho6bvJOfsjnS1BbkMkaTZ4MYT9WrQiDvGDbFTsPjF7W9MJW0zSGmMLMy1h2yG_vyi0pT-qHkagdXyVyEwQ6WqtVP9RFVVzARGQk6KIC-V8u0UA_HcoSlUqyrBRJ0mTy8h831-iNlNT-qmDsF2_eWqnkrBMuxqTwPHzk18spkPnPb4NEEH_2lUqmVvACA47wrE14z8Ed3vvfQiH5bMFN_tMjcjqe42vh6MtDbcj4_1WHlmxZbh5N_9vjmhoGj15NKEG.',
  'referer': 'https://detail.tmall.com/'
}


'''
反扒三种可能
1、浏览器伪装不够
2、请求频率过快、IP异常、触发验证
3、请求参数异常、触发验证

这个例子的sign直接复制会请求异常
经验所谈:sign长度是32位，多半是md5加密
参考上级目录的图片，构建sign
h函数就是md5加密函数
token是固定的
i是时间戳(动态)自己构建
g是appKey(固定)
data(固定)
'''

def get_sign(token:str, i:str, g:str, data:str):
  d = f'{token}&{i}&{g}&{data}'
  return md5(d.encode('utf-8')).hexdigest()




def get_data():
  t = int(time.time() * 1000)
  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
  print(t)
  url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/'
  token = '759d02c0f7d88c9472dce6434361f228',
  data='{"appId":"34385","params":"{\"device\":\"HMA-AL00\",\"isBeta\":\"false\",\"grayHair\":\"false\",\"from\":\"nt_history\",\"brand\":\"HUAWEI\",\"info\":\"wifi\",\"index\":\"4\",\"rainbow\":\"\",\"schemaType\":\"auction\",\"elderHome\":\"false\",\"isEnterSrpSearch\":\"true\",\"newSearch\":\"false\",\"network\":\"wifi\",\"subtype\":\"\",\"hasPreposeFilter\":\"false\",\"prepositionVersion\":\"v2\",\"client_os\":\"Android\",\"gpsEnabled\":\"false\",\"searchDoorFrom\":\"srp\",\"debug_rerankNewOpenCard\":\"false\",\"homePageVersion\":\"v7\",\"searchElderHomeOpen\":\"false\",\"search_action\":\"initiative\",\"sugg\":\"_4_1\",\"sversion\":\"13.6\",\"style\":\"list\",\"ttid\":\"600000@taobao_pc_10.7.0\",\"needTabs\":\"true\",\"areaCode\":\"CN\",\"vm\":\"nw\",\"countryNum\":\"156\",\"m\":\"pc\",\"page\":1,\"n\":48,\"q\":\"%E8%93%9D%E7%89%99%E8%80%B3%E6%9C%BA\",\"qSource\":\"url\",\"pageSource\":\"a21bo.jianhua/a.search_manual.0\",\"channelSrp\":\"\",\"tab\":\"all\",\"pageSize\":48,\"totalPage\":100,\"totalResults\":4800,\"sourceS\":\"0\",\"sort\":\"_coefp\",\"bcoffset\":\"\",\"ntoffset\":\"\",\"filterTag\":\"\",\"service\":\"\",\"prop\":\"\",\"loc\":\"\",\"start_price\":null,\"end_price\":null,\"startPrice\":null,\"endPrice\":null,\"itemIds\":null,\"p4pIds\":null,\"p4pS\":null,\"categoryp\":\"\",\"ha3Kvpairs\":null,\"myCNA\":\"leNXIIW0Ox4CAXdgON5DhO1o\",\"screenResolution\":\"1920x1080\",\"userAgent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36\",\"couponUnikey\":\"\",\"subTabId\":\"\",\"np\":\"\"}"}'
  params = {
    "jsv": "2.7.5",
    "appKey": "12574478",
    "t": '1752657535479',
    "sign": "59bf28a9417c0fc25b074f67578bde92",
    "api": "mtop.taobao.rate.detaillist.get",
    "v": "6.0",
    "isSec": "0",
    "ecode": "1",
    "timeout": "20000",
    "type": "jsonp",
    "dataType": "jsonp",
    "jsonpIncPrefix": "pcdetail",
    "callback": "mtopjsonppcdetail23",
    "data": '{"showTrueCount":false,"auctionNumId":"719878428996","pageNo":1,"pageSize":20,"rateType":"","searchImpr":"-8","orderType":"","expression":"","rateSrc":"pc_rate_list"}'
  }
  response = requests.get(url, headers=headers, params=params)
  print(response.text)


if __name__ == '__main__':
  get_data()




