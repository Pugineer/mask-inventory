import os
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.static import serve



def index(request):
    return render(request, 'hktvmall/index.html')