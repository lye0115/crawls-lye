import requests
from hashlib import md5
import time

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
  'cookie':'thw=cn; _hvn_lgc_=0; tracknick=tb17200_45; havana_lgc2_0=eyJoaWQiOjgyNDUwMjU4NCwic2ciOiIzYTZlNDI5YTVkMTgzMjQxYzYwYmEyMmNmOTUxMTEwMCIsInNpdGUiOjAsInRva2VuIjoiMWF3QUhKelNwX1FxcGRIZ3dmTWl1RncifQ; wk_cookie2=1342e260925ef96ff8ee72fb444fc947; wk_unb=W8twr6MPjEz5; useNativeIM=false; wwUserTip=false; cna=leNXIIW0Ox4CAXdgON5DhO1o; _samesite_flag_=true; cookie2=16c78766e7d5291b2c695da21313cf02; t=c94dfb5772c487fee46a93792483dd09; _tb_token_=ee4e3eee5ee8e; sn=; lgc=tb17200_45; cancelledSubSites=empty; dnk=tb17200_45; cnaui=824502584; aui=824502584; isg=BEtLnp42p086M_QWXFfseo9C2uk14F9iJvg4vr1IPArE3Gs-RbbZsutvtNwyBrda; miid=118027507489245424; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zMG1aAN%2F1UrnbH18zE9KTygW11QdYfVQqHnGms3HovfhWHj7Pt29rPiQxxqoSW%2B0wxIUUmlSlkg4wQXEdQItWUxWI34xHMD6OAL%2BxDyrHBsXD%2Fp244pFOlnIv4XoffhN2u75T6VC5VsPxYKO6P3rtXP4WcqCFB070xb7RNwXRrGAip28mPZrTwzwtZInvj7oSHWAO94Uz1Z801yaxqeaOc45nB5%2FDBu9w01EeYXy2OoKgs6YmWwYXUydSywC4MjauvlqYO%2BU7fyLJ0HgUgrjtO2yt4ID1SmqMcSONLz3hapX%2BdBB9EvqicKty3s5zo90KxNoNiA21b0TySxIqIUq3NKHdh5ROpxNhs0Gaaa8Pd%2BuvDYnnXtyVbHBCDfADHU4HjJ4FtI8yeoyW1DJJRWM9pk9boweaazba%2B4w1hlZ4ZxE7AJtNerzw%2BJcsMa4bEKR2dv%2BZP7WR2CroZPIetETGhM3821zG6RpVlOzwe5kRvtIUTVLY5XyesZEQgskNN4eyA%2Ba03XM4UJV%2FyJTFk%2FjQQC8jWEVL7gEt4lXBvy0sLbq2g6IIds8wRjzAttb1EKsxIIduEqVpVz0vd20Hcfrh4qSVc%2FYPj99KXI7dLtdW5466cFmAotnDvCR6KhBCj4uIsjqHMi1wVSJCqb%2FEwnVCC9TMHbzFz7G6b4mXd4GcvXUaeBRSkmqQXnPJTaoSe2MyqRM5471njKRh8krEOGlTHP4WsIay4fmIUJ4spxfUf2ujaLycptYy0r1t49YKj8SoXuvSEqgd11VyOQn43NaKOVGmuJ%2BqCIFx3ggAvQKaL66fPnBljBeiHMi1sVGpVAEmnEDKCSlVCRMlMZtDclZBNR%2B0CpUJkZ9kIxRZxwe2MGU5%2FW4thWh4tWSsIIJAnWBaXwDvmYoGxnKsBBwN%2FQpd6%2BqWv7QHM72oQvYt%2BDPX00xJ0vCEpTf%2FqRFBmHbYi7JYKVJ0SnrFABv4TPy9rtO12y%2FQJ9OVxxIZVp%2BfXwmjzkhxtWeX4sc91HRKKaMMzPGowRfW4QOq0kMm9N04fQ9ukP1nDxv1eBVWl%2FG5k9zhpx1MRHXb0CayJFUzxtT%2BJC0nqR%2B50lymmih2XAc08RwQLq2nj; tkSid=1752566500612_556863009_0.0; mtop_partitioned_detect=1; _m_h5_tk=c3b3154b769d976f7b463a6067ace42e_1752574062401; _m_h5_tk_enc=c71e74edbd5c3121f0aeca6a0d83253d; bxuab=0; sgcookie=E100IsR5mgy4rN4%2Bac16ZN8jw9wIE1BSx7qkGhmFXSE96KS9S6SX4R8j0FNKxD6Hs9ThycS5LpNLFJ1Awr%2FFV657PHzEUlOD8R5VXl%2FU325xGzgeQcL80cwvQ1sjP57a722d; cookie3_bak=16c78766e7d5291b2c695da21313cf02; cookie3_bak_exp=1752825703721; havana_lgc_exp=1783670503724; unb=824502584; uc1=pas=0&cookie14=UoYbySQkOvRT8g%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=WqG3DMC9VAQiUQ%3D%3D; uc3=id2=W8twr6MPjEz5&vt3=F8dD2fpgw4HZzFCkssg%3D&nk2=F5REOWeEfJ%2BaPw%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; csg=be517526; env_bak=FM%2BgmZzCKPPmPiNCG%2BcmEZpsWbj6fuTn%2B55U44uqbAfO; cookie17=W8twr6MPjEz5; skt=a9d40fe5012a4c5e; existShop=MTc1MjU2NjUwMw%3D%3D; uc4=id4=0%40WeiuNI76Yw2Pp4%2BDDvl0Ytu0lKg%3D&nk4=0%40FY4PawtB%2Bp3J0Ash0U884ltC9Bt6; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=548; _nk_=tb17200_45; cookie1=W8zOT%2F%2FlhP%2FunSF5b2tj9M5fBqrRm9qW056DR5UFi%2BY%3D; sdkSilent=1752652903729; havana_sdkSilent=1752652903729; xlly_s=1; tfstk=g5MrLMwEdJ0XQhU8ZxwF77SrWiw8dJ8stvaQxDm3Vz4kwbG4x2gvv3eSxyuElrBSNQFQ8MzmzWMB29GVYc3q8WK8Ry4ERDcWcd9s20eLKX86CdTE4phnUybQK8eDs9Ut1d9s20j7qhiDCv1Hy9U0-JVur-X0klf3q2VuiS4YvkbuxTx20rELqg4hZi202le3-22H0m4YxJqo-Jc-Q0mh3lNkmcr3nfvTL7ziqrWZDxquV_nuuTWr3mNzSpzVK9D44DlIvyBkQrcStYwmEEj_nchjroywUNEricyu42pOe8mimXVrLBsTJjom1SlAVHUK3mDotmQymRoqGfNrgUXUlYaY6Y2e_gEjUmDTTYLPnzuxmfw-IEBESmiseSHe7Z4KNle0YvKGTyPh4DbLmjFEpb7hT7qY0Pt20Zm_U5w_kuZR96F0Boz6Vu1d97zg0PtWV6CLiyq453Z5.',
  'referer': 'https://ai.taobao.com/'
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
    'jsv': '2.7.4',
    'appKey': '12574478',
    't': t,
    'sign': get_sign(token, t, '12574478', data),
    'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
    'v': '2.0',
    'timeout': '10000',
    'type': 'jsonp',
    'dataType': 'jsonp',
    'callback': 'mtopjsonp5',
    'data': data,
    'bx-ua':'231!xqv3UAmUtiB+j38+dk7mpzBjUGg0uSOn+fYFmLQQwGng0wmHntUSK+2ttWIwYfiRlXeQ+thKJXIvfegh2cGUuRIvbZ9fhRfZbrcyCwJp1Tn/1O6FZpEGdja43/LWLg1cKp0L8NMkYFMtE16p45ZivZA1pT29tq/HAA677E6EdQCeq1iAv2YSC/O+iUHmH4IEOs4Pc3dmFfC6zG/CP/rJgf5g2tf4D2G2qaSZOImetm4h5VjKGFh/ziD+iu8n+Zd++6WF1csd0l8LHJBh+++j+ygU3+jOL6/IR5j9Fkk3HC0i0AVEQN+QS8SjhoCJTiKu4lazbS6t6BFY6bQ3b5JtkcQfXVt/kPFwnwnxJ/D49D+F9gmKru0IQGsNYrhM2dzR8qPHp/NukE1AYL8LMg+4zSwH4x3dMZ7vjpPLqLwXoUrdlG9cUHBNHVa4e9kNvaII8wXw6QErYqA8SS/PVGr8dQT5aS5hT6lLZT0Ot641WxWM+W1Xj9NtZYEfuPCLUFzQ3+jZdVIw9ygw8ELDsdPapFtZtGHliqH+sWJAEVPek+lbL5AetSOgI7fnpG98+WgEOxF2AExOxLygts/AlrccsxlNpOQQnilRvnUbxb3kPV1/j87gYrwmHk0Jej04wgVCYEZxL+WSoiiD0hyfZWO8/p8S6GBjXFtr+nVmKNmQ7XkjYsWUKUQug9l6+Whg5wDhLHe1JBOnMZbekP4tSNphm9H7gqsATEcM5VyOAiJq+13C8zrYVWAm3IXdGYpyR9i1UTR0ucoxpZtU+b/MYu3G/+3jmj1QC7Lk20m6GbIzElXUTW0c3ADn3mJJFn5KWL0ctFailFcY0qdlavI19+o2JDr8jUf/9GkajZt2latlhkH/TlPqH947A6NjgJBioQW/f2NmSUfiUuGwL/hGmCBRSpB2XuRcsvDsx1z7n9H4bgGZ3Xye1IZtd9IXXThfuSz2F6utFJDU2pCVnJKt4g0qvqtzU9LvWl2v7dHEx3qZuLvYBa45uIFAfEcyv5AWOwZn4T3FRuTb2eDktNYmI2YxRkdtXco9bYIfu6TqRyEKO0Ze0CU9I32v1bXMGp1c9OprXrKoWygqFzOzdNqJkWCa/y8EHAB2/bn4TxBBaYnsC+/bIqP/IgrlZRGEzUpeDB1P6wfhRWNDsqx/1OerRRa9wrCfFnGVd3VCJZCnVIyc0lzMo6AE1tcqlCFpnTmpDySZ7E/4/uFaoUMyyuo6xdhylzr/eA2L39NnrwVdWulj/y9bMu/kwpCf/dqWsCKeDpV2qTy4DomKZlvr9z97gPNE/wCdYj2u5u2o3fqQ6ODOP6F71St3UsZAVRqxLyunr4fiXOWHRmPKgcTrbOHIP7GxFDuuVAmwcPt64VRTNUzfxKV7z6wbwMUxYWIZ7RqUYnuFjPSzFr+eBEI9L2u5DGsRvpO+x1l1CTTY5eoq2Pr6ZI/LnfliMDEp64+jsOxWh3fSvtEwgevXBdu3ASiScBU5OY8WHmhCZrSgcvp2A/W6LwT+AJm1sZL3WssnR8hvqPo1XBRE2KAMIirP0RZ+XFCKKk27iecscitAtUIvk9sAsCGuB86u/25i1+Lj+4==',
    'bx-umidtoken':'T2gA9dDohmh8SJRp24xpF36VvE3Kejj3R8fvAXdKIUhk96m8X2DhuNblFNVheHoSzYg=',
    'bx_et':'gPkqw12ZCR0WYMaYiYwN8lS_BF2YdR8B3Aa_jcmgcr40lcqgQ406DriMkVkarchXD5TAbiHr8O6XkInGQRwMRe9BdmCYBRYCWUqL-rEtqPx7iZo0Hi2MRe9CNgVvlR01lVsZU_qLroqgj5xzrkq_IlXmSzVuxk_0IV0gE0qavPb0jrqlrzEgIP0gI3yuylwgSbUrmcXzASxolfdGkaZLgym0z9o-UoVlMm4PIODraSzhFzWGIYrmVMs3btvUrjGih8DDrMwovbg04JJVJoloY-qqWpBYnDmosSkw1MUta0cQabIXXPHrqxci2Z-uL0lSOSlyoOzShzFKnRRFDuMqqvFZHEWuu4noO-HHyOunVDMYwA8FrPhbv8qZBHfa75jybNEow5ktgNfaiuEzR3-PrDw4OSUcC91O672L4ytbc1CTgyqzRntf61FuSuzBco1..'
  }
  response = requests.get(url, headers=headers, params=params)
  print(response.text)


if __name__ == '__main__':
  get_data()




