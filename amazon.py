import json
import logging
import os
from datetime import datetime
from S3Upload import upload_file
from driver import initBrowser

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

def crawlAmazon():
    start = datetime.now()
    jsonDict = []
    error = False
    priceNotFound = False
    driver = initBrowser()
    driver.get("https://www.amazon.com/s?k=mask&ref=nb_sb_noss")
    terminate = False
    while not terminate:
        element = WebDriverWait(driver, 120).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.a-section.a-spacing-medium")))
        productWrapper = driver.find_elements_by_css_selector("div.a-section.a-spacing-medium")
        for product in range(len(productWrapper) - 1):
            print("Product " + str(product))
            totalPrice = 0
            if len(productWrapper[product].find_elements_by_css_selector("div.a-row.a-spacing-micro")) == 0:
                title = productWrapper[product].find_element_by_css_selector("span.a-size-base-plus.a-color-base.a-text-normal").text
                try:
                    priceWhole = productWrapper[product].find_element_by_class_name("a-price-whole").text
                    priceFraction = productWrapper[product].find_element_by_class_name("a-price-fraction").text
                except NoSuchElementException:
                    print("Item " + str(product) + ": Price not found.")
                productURL = productWrapper[product].find_element_by_class_name("a-link-normal").get_attribute("href")
                totalPrice = priceWhole + "." + priceFraction
                retrieveTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                jsonDict.append({"RetrieveTime": retrieveTime, "Title": title, "Price": totalPrice, "URL": productURL})
                print(title, totalPrice, productURL)

        nextPageBtn = driver.find_element_by_class_name("a-last")
        if len(driver.find_elements_by_css_selector("li.a-disabled.a-last")) == 0:
            nextPageBtn.click()
            with open(os.getcwd() + '/json/amazon.json', 'w', encoding="utf-8") as outfile:
                json.dump(jsonDict, outfile, ensure_ascii=False, indent=2)
        else:
            terminate = True

    if not error:
        print(datetime.now() - start)
        upload_file(os.getcwd() + '/json/amazon.json', "mask-inventory/amazon.json")
    return 0