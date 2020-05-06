import os

# Create your views here.
from django.views.static import serve
from hktv import crawlHKTV
from django.shortcuts import render
from rq import Queue
from worker import conn
q = Queue(connection=conn)


def index(request):
    return render(request, 'hktvmall/index.html')

def result(request):
    filepath = os.getcwd() + "/hktv.json"
    if not os.path.isfile(filepath):
        q.enqueue(crawlHKTV())
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

