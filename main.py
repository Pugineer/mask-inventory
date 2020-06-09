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
    mp.set_start_method('spawn')
    q = mp.Queue()
    p1 = mp.Process(target=crawlHKTV, args=(0, q))
    p1.start()
    p2 = mp.Process(target=crawlHKTV, args=(5, q))
    p2.start()
    p3 = Process(target=crawlHKTV, args=(10, q))
    p3.start()
    p4 = Process(target=crawlHKTV, args=(15, q))
    p4.start()
    p5 = Process(target=crawlHKTV, args=(20, q))
    p5.start()
    p6 = Process(target=crawlHKTV, args=(25, q))
    p6.start()
    p7 = Process(target=crawlHKTV, args=(30, q))
    p7.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    print(q.get())
    with open(os.getcwd() + '/json/HKTVMall.json', 'w', encoding="utf-8") as outfile:
        json.dump(q.get(), outfile, ensure_ascii=False)
