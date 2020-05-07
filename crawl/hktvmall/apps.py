from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from hktv import crawlHKTV
from datetime import datetime


class HktvmallConfig(AppConfig):
    name = 'hktvmall'

    def ready(self):
        sched = BackgroundScheduler()

        @sched.scheduled_job('interval', minutes=3)
        def timed_job():
            print('This job is run every three minutes.')
            crawlHKTV()

        sched.start()
