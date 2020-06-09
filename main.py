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
    processes = []
    while length < 31:
        p = mp.Process(target=crawlHKTV, args=(length, q))
        processes.append(p)
        length += 5
        p.start()

    for p in processes:
        jsonDict += q.get()
        p.join()

    print(jsonDict)
    with open(os.getcwd() + '/json/HKTVMall.json', 'w', encoding="utf-8") as outfile:
        json.dump(jsonDict, outfile, ensure_ascii=False)

    watsonProc = mp.Process(target=crawlWatsons)
    watsonProc.start()
    hktvPigProc = mp.Process(target=crawlHKTVPig)
    hktvPigProc.start()
    watsonProc.join()
    hktvPigProc.join()