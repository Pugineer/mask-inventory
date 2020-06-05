import datetime as datetime

from watsons import crawlWatsons
from hktv import crawlHKTV, crawlHKTVPig
from apscheduler.schedulers.blocking import BlockingScheduler


def schedule():
    crawlHKTVPig()

sched = BlockingScheduler()
sched.add_job(schedule, 'interval', minutes=1, next_run_time=datetime.datetime.now())
sched.start()
