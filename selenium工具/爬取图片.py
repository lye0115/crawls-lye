from concurrent.futures import ThreadPoolExecutor
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def download_image(href):
    options = webdriver.ChromeOptions()
    # 启用无头模式
    options.add_argument('--headless')
    # 创建WebDriver对象
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # 打开链接
    browser.get(href)
    # 获取图片地址
    img_url = browser.find_element(By.CSS_SELECTOR, "#wallpaper").get_attribute("src")
    browser.quit()
    # 下载图片
    print('开始下载图片',img_url)
    response = requests.get(img_url)
    # 图片名称
    img_name = img_url.split('/')[-1]
    image_dir_path = os.path.join(os.path.dirname(__file__), "./assets/wallhaven")
    with open(f"{image_dir_path}/{img_name}", "wb") as f:
        f.write(response.content)
        print('下载完成',img_name)

def download_images(url,threadCount = 5):
    image_dir_path = os.path.join(os.path.dirname(__file__), "./assets/wallhaven")
    if not os.path.exists(image_dir_path):
        os.makedirs(image_dir_path)
    options = webdriver.ChromeOptions()
    # 启用无头模式
    options.add_argument('--headless')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get(url)
    elements = browser.find_elements(By.CSS_SELECTOR, ".preview")
    hrefs = [element.get_attribute("href") for element in elements]
    browser.quit()
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=threadCount) as executor:
        futures = executor.map(download_image, hrefs)
    end_time = time.time()
    print('下载完成,总共用时：',(end_time - start_time).round(2),'秒')


if __name__ == "__main__":
    download_images("https://wallhaven.cc/hot?page=3")


