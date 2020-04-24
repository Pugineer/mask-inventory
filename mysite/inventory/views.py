from django.shortcuts import render
from main import crawl
# Create your views here.
from django.http import HttpResponse


def index(request):
    context = crawl()
    return render(request, 'inventory/index.html', context)