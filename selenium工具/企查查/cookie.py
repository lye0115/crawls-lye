import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # options.add_argument('--headless')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    browser.get('https://aiqicha.baidu.com/?from=pz')
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    all_cookies = browser.get_cookies()
    for cookie in all_cookies:
        print(cookie)
    browser.quit()
if __name__ == "__main__":
    main()
