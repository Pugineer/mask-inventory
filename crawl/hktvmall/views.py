import os

# Create your views here.
from django.http import HttpResponse
from django.views.static import serve
from hktv import crawlHKTV
from django.shortcuts import render
from rq import Queue
from worker import conn
q = Queue(connection=conn)
filepath = os.getcwd() + "/hktv.json"
if not os.path.isfile(filepath):
    q.enqueue(crawlHKTV())

def index(request):
    if not os.path.isfile(filepath):
        q.enqueue(crawlHKTV())
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

