# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *


def index(request):
    return render(request, 'mbti/index.html')



def printQuestion(request, quesNum):
    num = int(quesNum)
    question_list = ["질문1","질문2","질문3","질문4","질문5","질문6","질문7","질문8","질문9","질문10"]

    if (num > 10):
        answer = request.GET['answer']
        new_answer = Answer(question_number = num, answer = answer)
        new_answer.save()
        return redirect('/mbti/result/')

    elif (num == 1):
        #answer 초기화
        answer_all = Answer.objects.all()
        answer_all.delete()

        ques = question_list[num-1]
        num += 1

    else:
        answer = request.GET['answer']
        new_answer = Answer(question_number = num, answer = answer)
        new_answer.save()
        ques = question_list[num-1]
        num += 1

    context = {'number' : num, 'question' : ques}
    return render(request, 'mbti/question.html', context)



def printResult(request):
    answer_list = []
    answer_all = Answer.objects.all()
    mbti = calculateMBTI(answer_all)
    answer_all.delete()

    content = {'mbti': mbti}
    return render(request, 'mbti/result.html', content)



def calculateMBTI(answer_list):
    mbti_list = [0,0,0,0]

    for i in range(len(answer_list)) :
        mbti_list[0] += answer_list[i].answer * i
        mbti_list[1] += answer_list[i].answer * i
        mbti_list[2] += answer_list[i].answer * i
        mbti_list[3] += answer_list[i].answer * i

    mbti = ""
    if mbti_list[0] > 50:
        mbti += "I"
    else:
        mbti += "E"
    if mbti_list[1] > 50:
        mbti +=  "N"
    else:
        mbti += "S"
    if mbti_list[2] > 50:
        mbti +=  "T"
    else:
        mbti += "F"
    if mbti_list[3] > 50:
        mbti +=  "P"
    else:
        mbti += "J"

    return mbti