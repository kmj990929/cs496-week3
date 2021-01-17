from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('success/', views.checkLogin, name="checkLogin"),
    path('signup/', views.signup, name="signUp"),
    path('signup/success/', views.checkSignup, name='checkSignup')
]