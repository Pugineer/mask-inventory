import datetime as datetime
import json
import os
from multiprocessing import Process, Queue
from watsons import crawlWatsons
from hktv import crawlHKTV, crawlHKTVPig
from amazon import crawlAmazon, crawlAmazonPig
from apscheduler.schedulers.blocking import BlockingScheduler

import multiprocessing as mp

if __name__ == '__main__':
    jsonDict = []
    mp.set_start_method('spawn')
    manager = mp.Manager()
    q = manager.Queue()
    length = 0
    testData = [(0, q), (5, q), (10, q), (15,q), (20,q), (25,q), (30,q)]
    pool = mp.Pool()
    pool.starmap(crawlHKTV, testData)
    pool.close()
    pool.join()

    print(jsonDict)
    with open(os.getcwd() + '/json/HKTVMall.json', 'w', encoding="utf-8") as outfile:
        json.dump(jsonDict, outfile, ensure_ascii=False)
