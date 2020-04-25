
from django.shortcuts import render
from .main import crawl

def index(request):
    context = {
        "crawlResult": crawl()
    }
    return render(request, 'inventory/index.html', context)