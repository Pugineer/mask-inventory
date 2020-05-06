import os

# Create your views here.
from django.views.static import serve
from hktv import crawlHKTV


def index(request):
    crawlHKTV()
    filepath = os.getcwd()
    filepath += "/hktv.json"
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
