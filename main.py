import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def crawl(productsList):
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    options = Options()
    options.binary_location = GOOGLE_CHROME_PATH
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    try:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
        print("run")
    except:
        driver = webdriver.Chrome()
        print("Exception")
    driver.get("https://www.hktvmall.com/hktv/zh/search_a?keyword=%E5%8F%A3%E7%BD%A9&bannerCategory=AA32250000000")
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "brand-product-name"))
    )
    products = driver.find_elements_by_class_name("brand-product-name")
    productList = []
    for p in range(len(products)):
        productList.append(products[p].text)

    return productsList

