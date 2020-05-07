import os

# Create your views here.
from django.http import HttpResponse
from django.views.static import serve

filepath = os.getcwd() + "/hktv.json"


def index(request):
    if not os.path.isfile(filepath):
        return HttpResponse("Crawling")
    else:
        return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
