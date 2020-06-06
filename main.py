import datetime as datetime

from watsons import crawlWatsons
from hktv import crawlHKTV, crawlHKTVPig
from amazon import crawlAmazon
from apscheduler.schedulers.blocking import BlockingScheduler


def schedule():
    crawlAmazon()

sched = BlockingScheduler()
sched.add_job(schedule, 'interval', hours=12, next_run_time=datetime.datetime.now())
sched.start()
