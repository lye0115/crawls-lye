from concurrent.futures import ThreadPoolExecutor
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree
import os
from multiprocessing import Pool


# 多线程
def download_chapter(url,browser,lock,dir_path):
    with lock:
        browser.get(url)
        title = browser.find_element(By.XPATH,'//*[@id="content_read"]/div/div[2]/h1').text
        print(f'开始下载{title}...')
        content_list = browser.find_elements(By.XPATH,'//*[@id="content"]/p')
        content = '\n\n'.join([content.text for content in content_list])
    with open(os.path.join(dir_path,f'{title}.txt'),'w',encoding='utf-8') as f:
        f.write(content)
        print(f'{title}.txt拉取完成')

def download_chapter_with_process(url):
    dir_path = os.path.join(os.path.dirname(__file__),'万族之劫')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
            browser.get(url)
            title = browser.find_element(By.XPATH,'//*[@id="content_read"]/div/div[2]/h1').text
            print(f'开始下载{title}...')
            content_list = browser.find_elements(By.XPATH,'//*[@id="content"]/p')
            content = '\n\n'.join([content.text for content in content_list])
            with open(os.path.join(dir_path,f'{title}.txt'),'w',encoding='utf-8') as f:
                f.write(content)
            break
        except Exception as e:
            print(f'下载或写入失败: {url}, 错误: {e}')
            return e


def main(url,novel_name,processes_num):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    browser.get(url)
    # 获取章节列表
    tree = etree.HTML(browser.page_source)
    chapter_list = tree.xpath('//*[@id="list"]/dl/dd[*]/a/@href')
    urls = [url + s_url.split('/')[-1] for s_url in chapter_list]
    lock = threading.Lock()
    # 创建目录
    dir_path = os.path.join(os.path.dirname(__file__),novel_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # with Pool(processes=processes_num) as pool:
    #     # executor.map(lambda url:download_chapter(url,browser,lock),urls)
    #     pool.map(download_chapter_with_process,urls)
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=processes_num) as executor:
        executor.map(lambda url:download_chapter(url,browser,lock,dir_path),urls)    
    end_time = time.time()
    print(f'下载完成，耗时: {end_time - start_time}秒')
    browser.quit()




if __name__ == '__main__':
    main('https://www.beqege.cc/16719/',novel_name='很纯很暧昧',processes_num=24)

