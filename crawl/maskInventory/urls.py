from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hktv.json', views.hktv, name='hktv'),
    path('wastons.json', views.wastons, name='wastons')
]