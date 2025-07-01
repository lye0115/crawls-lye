from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os

chromedriver_path = os.path.join(os.path.dirname(__file__), '../chromedriver-mac-x64/chromedriver')

# 配置信息
options = webdriver.ChromeOptions()
# 启用无头模式
# options.add_argument('--headless')

# 创建WebDriver对象
browser = webdriver.Chrome(service=Service(f'{chromedriver_path}'),options=options)

# 打开百度
browser.get("https://wallhaven.cc/toplist?page=9")

print(browser.title)

browser.save_screenshot('./assets/baidu.png')

browser.quit()
