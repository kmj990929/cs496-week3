from django.conf.urls import url, path

from . import views

urlpatterns = [
    url('', views.index),
    path('question/', vies.printQuestion, name="home"),
    path('result/', views.printResult, name="result"),
]