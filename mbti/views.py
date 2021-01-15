# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



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
    artist = matchArtist(mbti)
    matchSongs(artist)
    answer_all.delete()

    song_all = Song.objects.all()

    content = {'match_artist': artist, 'song_list' : song_all}
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

def matchArtist(mbti):
    if (mbti == "INTP") :
        return "iu"
    else :
        return "AKMU"

def matchSongs(artist):
    song_list = []
    #chrome 띄우지 않고 백그라운드에서 selenium 크롤링
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

    driver = webdriver.Chrome('C:/Users/q/Desktop/chromedriver.exe', chrome_options=chrome_options)
    url = "https://www.youtube.com/results?search_query="
    url += artist+"+mv"
    driver.get(url)

    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'lxml')
    all_link = soup.find_all('a','yt-simple-endpoint style-scope ytd-video-renderer')
    all_thumbnail = soup.find_all('a','yt-simple-endpoint inline-block style-scope ytd-thumbnail')
    for i in range(4):
        song_url = "https://www.youtube.com/embed/"
        idx = all_link[i].attrs['href'].index("=")
        song_url += all_link[i].attrs['href'][idx+1:]
        song_thumbnail = all_thumbnail[i].find('yt-img-shadow').find('img').attrs['src']
        song_title = all_link[i].attrs['title']

        ### 노래 db에 추가 ###
        new_song = Song(url = song_url, title = song_title, thumbnail = song_thumbnail)
        new_song.save()


    