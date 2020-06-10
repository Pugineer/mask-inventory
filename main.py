import datetime as datetime
import json
import os
from multiprocessing import Process, Queue

from S3Upload import upload_file
from watsons import crawlWatsons
from hktv import crawlHKTV, crawlHKTVPig
from amazon import crawlAmazon, crawlAmazonPig
from apscheduler.schedulers.blocking import BlockingScheduler
from itertools import chain

import multiprocessing as mp

if __name__ == '__main__':
    jsonDict = []
    mp.set_start_method('spawn')
    manager = mp.Manager()
    q = manager.Queue()
    length = 0
    testData = [0,5,10,15,20,25,30]
    pool = mp.Pool()
    result = pool.map_async(crawlHKTV, testData)
    pool.apply_async(crawlAmazon)
    pool.apply_async(crawlAmazonPig)
    pool.apply_async(crawlWatsons)
    pool.apply_async(crawlHKTVPig)
    jsonDict = list(chain(*result.get()))
    with open(os.getcwd() + '/json/HKTVMall.json', 'w', encoding="utf-8") as outfile:
        json.dump(jsonDict, outfile, ensure_ascii=False, indent=2)

    pool.close()
    pool.join()


    upload_file(os.getcwd() + '/json/HKTVMall.json', "mask-inventory/HKTVMall.json")
