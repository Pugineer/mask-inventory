import json
import logging
import os
from datetime import datetime
from S3Upload import upload_file

import boto3 as boto3
from botocore.exceptions import ClientError
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from urllib3 import request


def crawlHKTV():
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    ua = UserAgent(verify_ssl=False)
    user_agent = ua.chrome
    # print("Booting with: " + user_agent)
    options = Options()
    options.binary_location = GOOGLE_CHROME_PATH
    options.add_argument("--lang=zh-TW");
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--headless")
    options.add_argument("--disable-plugins")
    # Image disable
    options.add_argument('blink-settings=imagesEnabled=false')

    # Bug avoid
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument("--disable-dev-shm-usage")
    start = datetime.now()
    try:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
        print("run")
    except:
        options.binary_location = ""
        driver = webdriver.Chrome(chrome_options=options)
        print("Exception")

    driver.get("https://www.hktvmall.com/hktv/zh/search_a?keyword=%E5%8F%A3%E7%BD%A9&bannerCategory=AA32250000000")

    terminate = False
    # Crawling HKTVMall
    pageNumber = 0
    jsonDict = []
    filterList = ["盒", "墊", "袋", "套", "夾", "液", "收納", "神器", "劑", "鏡", "寶", "機", "帽", "霧", "掛頸", "啫喱", "肌", "貼"]
    while not terminate:
        pageNumber += 1
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "brand-product-name")))

        print("Crawling on page " + str(pageNumber) + "...", end="   ")
        productWrapper = driver.find_elements_by_class_name("product-brief-wrapper")

        for p in range(len(productWrapper)):
            product = productWrapper[p].find_element_by_class_name("brand-product-name").text
            if not any(word in product for word in filterList):
                price = (productWrapper[p].find_element_by_class_name("sepaButton.add-to-cart-button").get_attribute(
                    "data-price"))
                url = (productWrapper[p].find_elements_by_css_selector("a")[1].get_attribute("href"))
                jsonDict.append({"Title": product, "Price": price, "URL": url})

        btn = driver.find_element_by_id("paginationMenu_nextBtn")
        if not btn.get_attribute("class") == "disabled":

            action = ActionChains(driver)
            action.move_to_element(btn).perform()
            driver.execute_script("window.scrollBy(0,100)")
            action.click().perform()
            print("Done.")
        else:
            terminate = True
            print("Done.")
            print("Crawling completed.")

    with open(os.getcwd() + '/HKTVMall.json', 'w', encoding="utf-8") as outfile:
        json.dump(jsonDict, outfile, ensure_ascii=False)

    print(datetime.now() - start)
    # Creating JSON file
    upload_file(os.getcwd() + '/HKTVMall.json', "mask-inventory/HKTVMall.json")
    driver.quit()
    return 0

