from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('question/<quesNum>/', views.printQuestion, name="question"),
    path('result/', views.printResult, name="result"),
]