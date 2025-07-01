# 问题描述：现在部分网站可以通过修改字体来反扒，这样爬取的文字无法识别
# 1.正则获取字体的下载地址
# 2.获取月票加密数据
# 3.清洗月票数据信息，因为数字混淆了其他特殊字符
# 4.解密数据
# 5.写入json文件

from concurrent.futures import ThreadPoolExecutor
import json
import os
import requests
import re
from io import BytesIO
from fontTools.ttLib import TTFont
from lxml import etree

num_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # 'Referer': 'https://www.qidian.com/',
    'Cookie':'e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A5%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C44%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A5%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C44%22%7D; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A5%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C44%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A5%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C44%22%7D; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A5%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C44%22%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A5%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_P_rank_19%22%2C%22eid%22%3A%22qd_C44%22%7D; _csrfToken=E0YgXGaYLSEBCx9wxb2rPN9Hy97l0nBCXqfYtYS2; traffic_utm_referer=https%3A//www.bing.com/; Hm_lvt_f00f67093ce2f38f215010b699629083=1734070228; HMACCOUNT=638CE3BEB64B3A18; newstatisticUUID=1734070228_1864713790; fu=63376145; _gid=GA1.2.70818880.1734070233; supportwebp=true; e1=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A11%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A118%22%2C%22l2%22%3A1%7D; e2=%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A11%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A118%22%2C%22l2%22%3A1%7D; _ga_FZMMH98S83=GS1.1.1734073944.2.1.1734075168.0.0.0; _ga=GA1.1.1789157564.1734070233; _ga_PFYW0QLV3P=GS1.1.1734073944.2.1.1734075168.0.0.0; Hm_lpvt_f00f67093ce2f38f215010b699629083=1734075169; w_tsfp=ltvuV0MF2utBvS0Q6q7pk06nHj8jcjw4h0wpEaR0f5thQLErU5mG1YZ9u8L/N3LZ58xnvd7DsZoyJTLYCJI3dwMTQp6TJosTjQXBldAnj4tAAhQ0Es7fXFVLcOpx6zZGKHhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5Tfdt1L7Lgh0VegU1UCU3CkWCn9w4xDuJ7wIYxuucJj+SqA='
}

# # 请求月票数据
# response = requests.get('https://www.qidian.com/rank/yuepiao/chn0/', headers=headers)

# # 获取字体链接
# font_url = re.findall(r"\); src: url\('(.*?)'\) format\('woff'\)", response.text)[0]

# # 查找混淆文本
# unread_text = re.findall(r'</style><span class=".*?">(.*?)</span></span>月票', response.text)[0]

# # 替换特殊字符
# unread_text = unread_text.replace('&#', '')

# # 以;进行分割乘列表并去除空白项目
# unread_text = [item for item in unread_text.split(';') if item.strip()]

# # 下载字体
# font_response = requests.get(font_url, headers=headers)
# font_data = BytesIO(font_response.content)
# font = TTFont(font_data)

# # 获取字体映射
# num_str = ''
# map = font.getBestCmap()


# for item in unread_text:
#     num_str += num_map[map[int(item)]]

# print(num_str)

def qidian_yuepiao(url):
    response = requests.get(url, headers=headers)
    # 处理月票数目
    yuepiao_nums = []
    # 获取字体链接
    font_url = re.findall(r"\); src: url\('(.*?)'\) format\('woff'\)", response.text)[0]
    # 下载字体,处理字体映射
    font_response = requests.get(font_url, headers=headers)
    font_data = BytesIO(font_response.content)
    font = TTFont(font_data)
    map = font.getBestCmap()
    # 查找混淆文本
    unread_texts = re.findall(r'</style><span class=".*?">(.*?)</span></span>月票', response.text)

    for unread_text in unread_texts:
        # 替换特殊字符
        unread_text = unread_text.replace('&#', '')
        # 以;进行分割乘列表并去除空白项目
        unread_text = [item for item in unread_text.split(';') if item.strip()]
        num_str = ''
        for item in unread_text:
            num_str += num_map[map[int(item)]]
        yuepiao_nums.append(num_str)

    # 转dom结构
    tree = etree.HTML(response.text)

    # 获取书名
    yuepiao_book_names = tree.xpath('//*[@id="book-img-text"]/ul/li[*]/div[2]/h2/a/text()')
    # 获取作者
    yuepiao_authors = tree.xpath('//*[@id="book-img-text"]/ul/li[*]/div[2]/p[1]/a[1]/text()')
    # 获取书的简介
    yuepiao_book_intros = tree.xpath('//*[@id="book-img-text"]/ul/li[*]/div[2]/p[2]/text()')
    # 最近更新时间
    yuepiao_book_update_times = tree.xpath('//*[@id="book-img-text"]/ul/li[*]/div[2]/p[3]/span/text()')
    # 小说类型
    yuepiao_book_types = tree.xpath('//*[@id="book-img-text"]/ul/li[*]/div[2]/p[1]/a[3]/text()')

    return [{'书名':yuepiao_book_names[i], '作者':yuepiao_authors[i], '简介':yuepiao_book_intros[i], '最近更新时间':yuepiao_book_update_times[i], '小说类型':yuepiao_book_types[i], '月票数':yuepiao_nums[i]} for i in range(len(yuepiao_book_names))]

def qidian_yuepiaos(base_url):
     urls = [f'{base_url}{page}/' for page in range(1,6)]
     with ThreadPoolExecutor(max_workers=5) as executor:
          futures = executor.map(qidian_yuepiao, urls)
          all_yuepiaos = []
          for future in futures:
               all_yuepiaos.extend(future)
     json_path = os.path.join(os.path.dirname(__file__), '起点月票.json')
     json.dump(all_yuepiaos, open(json_path, 'w', encoding='utf-8'), ensure_ascii=False)          
    



if __name__ == "__main__":
      qidian_yuepiaos('https://www.qidian.com/rank/yuepiao/chn0/year2024-month12-page')