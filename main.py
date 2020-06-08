import datetime as datetime
from multiprocessing import Process
from watsons import crawlWatsons
from hktv import crawlHKTV, crawlHKTVPig
from amazon import crawlAmazon
from apscheduler.schedulers.blocking import BlockingScheduler


if __name__ == '__main__':
    def schedule():
        p1 = Process(target=crawlWatsons)
        p1.start()
        p2 = Process(target=crawlHKTV)
        p2.start()
        p3 = Process(target=crawlHKTVPig)
        p3.start()

    sched = BlockingScheduler()
    sched.add_job(schedule, 'interval', hours=12, next_run_time=datetime.datetime.now())
    sched.start()
