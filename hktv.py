import json
import os
import gc
import time
from datetime import datetime

from selenium.common.exceptions import TimeoutException, NoSuchElementException

from S3Upload import upload_file
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from driver import initBrowser


def crawlHKTV():
    start = datetime.now()
    jsonDict = []
    prevURL = ""
    error = False
    driver = initBrowser()
    driver.get("https://www.hktvmall.com/hktv/zh/search_a?keyword=%E5%8F%A3%E7%BD%A9&bannerCategory=AA32250000000")

    # Crawling HKTVMall
    init = True
    filterList = ["盒", "墊", "袋", "套", "夾", "液", "收納", "神器", "劑", "鏡", "寶", "機", "帽", "霧", "掛頸", "啫喱", "肌", "貼"]
    element = WebDriverWait(driver, 120).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "brand-product-name")))
    countryLabel = driver.find_element_by_xpath("//*[contains(text(), '顯示全部產地')]")
    countryLabel.click()
    time.sleep(1)
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    checkboxWrapper = driver.find_element_by_class_name("ui-grid-view")
    checkbox = checkboxWrapper.find_elements_by_class_name("list-label")
    print(len(checkbox))
    data = 0
    while data < len(checkbox):
        if not init:
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "brand-product-name")))
            countryLabel = driver.find_element_by_xpath("//*[contains(text(), '顯示全部產地')]")
            countryLabel.click()
            time.sleep(1)
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
            checkboxWrapper = driver.find_element_by_class_name("ui-grid-view")
            checkbox = checkboxWrapper.find_elements_by_class_name("list-label")

        resetBtn = driver.find_element_by_xpath("//*[contains(text(), '重設')]")
        submitBtn = driver.find_element_by_xpath("//*[contains(text(), '搜尋貨品')]")
        action = ActionChains(driver)
        action.move_to_element(resetBtn).click().perform()
        checkboxInput = checkbox[data].find_element_by_tag_name("input")
        action = ActionChains(driver)
        action.move_to_element(checkboxInput).click().perform()
        country = checkbox[data].text
        action = ActionChains(driver)
        action.move_to_element(submitBtn).click().perform()
        terminate = False
        pageNumber = 0
        print("Current country: " + country)

        while not terminate:
            pageNumber += 1
            print("Crawling on page " + str(pageNumber) + "...", end="   ")

            # Bug avoiding measure
            if driver.current_url == prevURL:
                print("Bug encountered, driver restarts. ")
                driver.quit()
                del driver
                driver = initBrowser()
                driver.get(
                    "https://www.hktvmall.com/hktv/zh/search_a?keyword=%E5%8F%A3%E7%BD%A9&bannerCategory=AA32250000000")
                data -= 1
                break

            element = WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "brand-product-name")))
            productWrapper = driver.find_elements_by_class_name("product-brief-wrapper")

            for p in range(len(productWrapper)):
                title = productWrapper[p].find_element_by_class_name("brand-product-name").text
                outOfStock = len(productWrapper[p].find_elements_by_class_name("out-of-stock-label")) > 0
                if not any(word in title for word in filterList) and not outOfStock:
                    price = (productWrapper[p].find_element_by_class_name("sepaButton").get_attribute(
                        "data-price"))
                    urlWrapper = productWrapper[p].find_elements_by_css_selector("a")

                    # Retrieving Store
                    store = productWrapper[p].find_element_by_class_name(
                        "store-name-label").find_element_by_css_selector(
                        "span").text

                    # Retrieving URL
                    for item in range(len(urlWrapper)):
                        if urlWrapper[item].get_property("rel") == "noopener" and urlWrapper[item].text == "":
                            url = urlWrapper[item].get_attribute("href")

                    # Retrieving time
                    retrieveTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    jsonDict.append({"RetrieveTime": retrieveTime, "Store": store, "Title": title, "Country": country,
                                     "Price": price, "URL": url})
                else:
                    price = ""
                    url = ""
                    retrieveTime = ""

            btn = driver.find_element_by_id("paginationMenu_nextBtn")
            prevURL = driver.current_url
            if not btn.get_attribute("class") == "disabled":
                action = ActionChains(driver)
                action.move_to_element(btn).perform()
                driver.execute_script("window.scrollBy(0,100)")
                action.click().perform()
                print("Done.")

                with open(os.getcwd() + '/json/HKTVMall.json', 'w', encoding="utf-8") as outfile:
                    json.dump(jsonDict, outfile, ensure_ascii=False, indent=2)

                # Release memory allocation
                del productWrapper, title, price, btn, element, url, retrieveTime, action, outfile
                driver.delete_all_cookies()
            else:
                terminate = True
                print("Done.")
                print("Crawling completed.")
                driver.quit()
                del driver
                if not data >= len(checkbox) - 1:
                    driver = initBrowser()
                    driver.get(
                        'https://www.hktvmall.com/hktv/zh/search_a?keyword=%E5%8F%A3%E7%BD%A9&bannerCategory=AA32250000000')

        data += 1
        init = False

    if not error:
        print(datetime.now() - start)
        upload_file(os.getcwd() + '/json/HKTVMall.json', "mask-inventory/HKTVMall.json")
    return 0


def crawlHKTVPig():
    start = datetime.now()
    driver = initBrowser()
    driver.get("https://www.hktvmall.com/hktv/zh/search_a?keyword=3m%20%E9%98%B2%E8%AD%B7%E9%9D%A2%E7%BD%A9")
    error = False
    terminate = False
    # Crawling HKTVMall
    pageNumber = 0
    jsonDict = []
    filterList = ["帽"]
    while not terminate:
        pageNumber += 1
        try:
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CLASS_NAME, "brand-product-name")))
        except TimeoutException:
            print("HKTVMall no response")
            error = True

        print("Crawling on page " + str(pageNumber) + "...", end="   ")
        productWrapper = driver.find_elements_by_class_name("product-brief-wrapper")

        for p in range(len(productWrapper)):
            product = productWrapper[p].find_element_by_class_name("brand-product-name").text
            if not any(word in product for word in filterList):
                price = (productWrapper[p].find_element_by_class_name("sepaButton").get_attribute(
                    "data-price"))
                url = (productWrapper[p].find_elements_by_css_selector("a")[1].get_attribute("href"))
                store = productWrapper[p].find_element_by_class_name("store-name-label").find_element_by_css_selector(
                    "span").text
                retrieveTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                jsonDict.append(
                    {"RetrieveTime": retrieveTime, "Store": store, "Title": product, "Price": price, "URL": url})
            else:
                price = ""
                url = ""

        btn = driver.find_element_by_id("paginationMenu_nextBtn")
        if not btn.get_attribute("class") == "disabled":

            action = ActionChains(driver)
            action.move_to_element(btn).perform()
            driver.execute_script("window.scrollBy(0,100)")
            action.click().perform()
            print("Done.")

            # Release memory allocation
            del productWrapper, product, price, element, url
        else:
            terminate = True
            print("Done.")
            print("Crawling completed.")

    if not error:
        with open(os.getcwd() + '/json/HKTVMallPig.json', 'w', encoding="utf-8") as outfile:
            json.dump(jsonDict, outfile, ensure_ascii=False)

        print(datetime.now() - start)
        # Creating JSON file
        upload_file(os.getcwd() + '/json/HKTVMallPig.json', "mask-inventory/HKTVMallPig.json")
    driver.quit()
    return 0
