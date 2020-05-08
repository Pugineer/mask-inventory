from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from hktv import crawlHKTV
from watsons import crawlWatsons
from datetime import datetime


class maskInventoryConfig(AppConfig):
    name = 'maskInventory'

    def ready(self):
        sched = BackgroundScheduler()

        def HKTV():
            print('This job is run every three minutes.')
            crawlHKTV()

        def Watsons():
            print('This job is run every three minutes.')
            crawlWatsons()


        sched.start()
