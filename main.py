import datetime as datetime
from multiprocessing import Process
from watsons import crawlWatsons
from hktv import crawlHKTV, crawlHKTVPig
from amazon import crawlAmazon, crawlAmazonPig
from apscheduler.schedulers.blocking import BlockingScheduler


def schedule():
    crawlWatsons()
    crawlHKTV()
    crawlHKTVPig()
    crawlAmazon()
    crawlAmazonPig()

sched = BlockingScheduler()
sched.add_job(schedule, 'interval', hours=12, next_run_time=datetime.datetime.now())
sched.start()
