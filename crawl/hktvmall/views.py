import os

# Create your views here.
from django.http import HttpResponse
from django.views.static import serve
from hktv import crawlHKTV


def index(request):
    return HttpResponse("Please wait")
