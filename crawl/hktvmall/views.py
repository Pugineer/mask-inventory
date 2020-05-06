import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.static import serve


def index(request):
    filepath = os.getcwd()
    filepath += "/hktv.json"
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
