from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from hktv import crawlHKTV
from watsons import crawlWatsons
from datetime import datetime


class maskInventoryConfig(AppConfig):
    name = 'maskInventory'

    def ready(self):
        sched = BackgroundScheduler()

        @sched.scheduled_job('interval', minutes=30, next_run_time=datetime.now())
        def timed_job():
            print('This job is run every three minutes.')
            crawlWatsons()

        sched.start()
