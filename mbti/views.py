# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'mbti/index.html')

def printQuestion(request):
    return render(request, 'mbti/question.html')

def printResult(request):
    #answer = request.GET['answer']
    return render(request, 'mbti/result.html')