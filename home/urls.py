from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('sharedmusic/', views.sharedMusic),
    path('goodSong/', views.goodSong),
    path('playlist/', views.playlist),
    path('checkGoodSong/', views.checkGoodSong)
]