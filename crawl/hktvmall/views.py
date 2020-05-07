from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.static import serve
from django.http import JsonResponse
import json
import os
with open(os.getcwd() + '/hktvmall/templates/hktvmall/hktv.json') as json_data:
    d = json.load(json_data)



def index(request):
    return render(request, 'hktvmall/index.html')

def hktv(request):
    return JsonResponse(d, safe=False)