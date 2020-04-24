from django.shortcuts import render

# Create your views here.
from main import crawl


def index(request):
    context = {
        "crawlResult": crawl()
    }
    return render(request, 'inventory/index.html', context)