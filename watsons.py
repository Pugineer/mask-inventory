import json
import logging
import os
from datetime import datetime
from S3Upload import upload_file

import boto3
from botocore.exceptions import ClientError
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time

def crawlWatsons():
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google-chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    ua = UserAgent(verify_ssl=False)
    user_agent = ua.chrome
    # print("Booting with: " + user_agent)
    options = Options()
    options.binary_location = GOOGLE_CHROME_PATH
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--headless")
    options.add_argument("--disable-plugins")
    options.add_argument("--lang=zh-TW")

    # Image disable
    # options.add_argument('blink-settings=imagesEnabled=false')

    # Bug avoid
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument("--disable-dev-shm-usage")
    error = False
    start = datetime.now()
    try:
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
        print("run")
    except:
        options.binary_location = ""
        driver = webdriver.Chrome(chrome_options=options)
        print("Exception")
    driver.maximize_window()
    driver.get("https://www.watsons.com.hk/search?text=%E5%8F%A3%E7%BD%A9")

    terminate = False
    # Crawling watson
    jsonDict = []
    retrieveTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    jsonDict.append({retrieveTime: []})
    while not terminate:
        try:
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CLASS_NAME, "productItemContainer")))
        except TimeoutException:
            print("Watsons no respond.")
            error = True
            break
        while len(driver.find_elements_by_link_text("顯示更多")) != 0:
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight - 20)")
            time.sleep(1)
            btn = driver.find_element_by_link_text("顯示更多")
            actions = ActionChains(driver)
            actions.click(btn).perform()
            time.sleep(3)
            print("Scrolling")

        productWrapper = driver.find_elements_by_class_name("productItemContainer")
        print(len(productWrapper))
        for p in range(len(productWrapper)):
            disable = (len(productWrapper[p].find_elements_by_link_text("售罄")) != 0) or (
                    len(productWrapper[p].find_elements_by_link_text("Out of stock")) != 0)
            if not disable:
                product = productWrapper[p].find_element_by_class_name("h1").text
                print(product)
                price = productWrapper[p].find_element_by_class_name("h2").text
                print(price)
                url = productWrapper[p].find_elements_by_css_selector("a")[0].get_attribute("href")
                print(url)
                jsonDict.append({"Title": product, "Price": price, "URL": url})
                print("Done.")

        terminate = True
        print("Crawling completed.")

    if not error:
        with open(os.getcwd() + '/watsons.json', 'w', encoding="utf-8") as outfile:
            json.dump(jsonDict[retrieveTime], outfile, ensure_ascii=False)

        print(datetime.now() - start)
        # Creating JSON file
        upload_file(os.getcwd() + '/watsons.json', "mask-inventory/watsons.json")
    driver.quit()

    return 0
