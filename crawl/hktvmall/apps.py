from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from hktv import crawlHKTV
from datetime import datetime
import os


class HktvmallConfig(AppConfig):
    name = 'hktvmall'
    def ready(self):
        crawlHKTV()
        pass