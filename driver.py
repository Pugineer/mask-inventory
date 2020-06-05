from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def initBrowser():
    ua = UserAgent(verify_ssl=False)
    user_agent = ua.chrome
    print("Booting with: " + user_agent)
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--headless")
    options.add_argument("--disable-plugins")
    options.add_argument("-lang=zh-TW")
    options.add_argument("--incognito")
    options.add_argument('--disable-extensions')

    # Image disable
    options.add_argument('blink-settings=imagesEnabled=false')

    # Bug avoid
    options.add_argument('--disable-gpu')

    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome( chrome_options=options)
    print("run")

    driver.maximize_window()

    # Make json dir
    path = os.getcwd() + "/json/"
    if not os.path.isdir(path):
        os.makedirs(path)
    return driver