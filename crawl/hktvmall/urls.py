from django.urls import path

from . import views
from apscheduler.schedulers.background import BackgroundScheduler
from hktv import crawlHKTV
from datetime import datetime

urlpatterns = [
    path('', views.index, name='index'),
]

sched = BackgroundScheduler()
@sched.scheduled_job('interval', minutes=3, next_run_time=datetime.now())
def timed_job():
    print('This job is run every three minutes.')
    try:
        crawlHKTV()
    except:
        print("Error occured")


sched.start()

