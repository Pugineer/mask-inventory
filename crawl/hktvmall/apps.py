from django.apps import AppConfig


class HktvmallConfig(AppConfig):
    name = 'hktvmall'

    def ready(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        from hktv import crawlHKTV
        from datetime import datetime
        crawlHKTV()
