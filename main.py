import datetime as datetime
import json
import os
from multiprocessing import Process, Queue
from watsons import crawlWatsons
from hktv import crawlHKTV, crawlHKTVPig
from amazon import crawlAmazon
from apscheduler.schedulers.blocking import BlockingScheduler

import multiprocessing as mp

if __name__ == '__main__':
    jsonDict = []
    mp.set_start_method('spawn')
    manager = mp.Manager()
    q = manager.Queue()
    length = 0
    while length < 31:
        p = mp.Process(target=crawlHKTV, args=(length, q))
        p.start()
        jsonDict += q.get()
        p.join()
        length += 5
    print(jsonDict)
    with open(os.getcwd() + '/json/HKTVMall.json', 'w', encoding="utf-8") as outfile:
        json.dump(jsonDict, outfile, ensure_ascii=False)
