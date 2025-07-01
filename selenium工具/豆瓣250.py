from concurrent.futures import ThreadPoolExecutor
import json
import os
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Lock

def get_movie_info(browser,lock, url):
    print(id(browser))
    with lock:
        browser.get(url)
        html = browser.page_source
        tree = etree.HTML(html)
        # 电影名
    movie_names = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a/span[1]/text()')
        # 电影评分
    movie_scores = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/div/span[2]/text()')
    # 电影简介
    movie_infos = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/p[2]/span/text()')
      # 电影海报
    movie_imgs = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[1]/a/img/@src')
    # 电影链接
    movie_links = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a/@href')
    # browser.quit()
    return movie_names, movie_scores, movie_infos, movie_imgs, movie_links

def main():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    movie_list = []
    urls = [f'https://movie.douban.com/top250?start={str(i)}&filter=' for i in range(0, 250, 25)]
    lock = Lock()
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = executor.map(lambda url: get_movie_info(browser,lock, url), urls)
        for future in futures:
            movie_names, movie_scores, movie_infos, movie_imgs, movie_links = future
            for name, score, info, img, link in zip(movie_names, movie_scores, movie_infos, movie_imgs, movie_links):
                movie_list.append({
                    'name': name,
                    'score': score,
                    'info': info,
                    'img': img,
                    'link': link
                })
    browser.quit()
    # json存放目录
    json_dir = os.path.join(os.path.dirname(__file__), './assets/json')
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)
    # 写入json文件
    with open(os.path.join(json_dir, '豆瓣250.json'), 'w', encoding='utf-8') as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=4)
if __name__ == "__main__":
    main()
