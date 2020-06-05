import json
import logging
import os
from datetime import datetime
from S3Upload import upload_file

import boto3
from botocore.exceptions import ClientError
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time
from driver import initBrowser

def crawlWatsons():
    start = datetime.now()
    error = False
    driver = initBrowser()
    driver.get("https://www.watsons.com.hk/search?text=%E5%8F%A3%E7%BD%A9")
    terminate = False
    jsonDict = []

    # Crawling watson
    while not terminate:
        element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CLASS_NAME, "productItemContainer")))

        while len(driver.find_elements_by_link_text("顯示更多")) != 0:
            driver.execute_script("window.scrollBy(0,document.body.scrollHeight - 100)")
            time.sleep(1)
            btn = driver.find_element_by_link_text("顯示更多")
            actions = ActionChains(driver)
            actions.click(btn).perform()
            time.sleep(3)

        productWrapper = driver.find_elements_by_class_name("productItemContainer")
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
                retrieveTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                jsonDict.append({"RetrieveTime": retrieveTime, "Title": product, "Price": price, "URL": url})
                print("Done.")

        terminate = True
        print("Crawling completed.")

    if not error:
        with open(os.getcwd() + '/json/watsons.json', 'w', encoding="utf-8") as outfile:
            json.dump(jsonDict, outfile, ensure_ascii=False)

        print(datetime.now() - start)
        # Creating JSON file
        upload_file(os.getcwd() + '/json/watsons.json', "mask-inventory/watsons.json")
    driver.quit()

    return 0
