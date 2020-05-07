from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.static import serve
from django.http import JsonResponse
import json
import os



def index(request):
    return render(request, 'maskInventory/index.html')

def hktv(request):
    with open(os.getcwd() + '/crawl/maskInventory/templates/maskInventory/hktv.json', encoding="utf-8") as json_data:
        d = json.load(json_data)
    return JsonResponse(d, safe=False)

def wastons(request):
    with open(os.getcwd() + '/crawl/maskInventory/templates/maskInventory/wastons.json', encoding="utf-8") as json_data:
        d = json.load(json_data)
    return JsonResponse(d, safe=False)
