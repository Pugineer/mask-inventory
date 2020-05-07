from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.static import serve
from django.http import JsonResponse
import json
import os



def index(request):
    return render(request, 'hktvmall/index.html')

def hktv(request):
    with open(os.getcwd() + '/crawl/hktvmall/templates/hktvmall/hktv.json', encoding="utf-8") as json_data:
        d = json.load(json_data)
    return JsonResponse(d, safe=False)