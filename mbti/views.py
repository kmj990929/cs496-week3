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
from . import calc
import random



def index(request):
    return render(request, 'mbti/index.html')



def printQuestion(request, quesNum):
    num = int(quesNum)
    question_list = ["질문1","질문2","질문3","질문4","질문5","질문6","질문7","질문8","질문9","질문10"]

    if (num > 10):
        answer = request.GET['answer']
        new_answer = Answer(question_number = num-1, answer = answer)
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
        new_answer = Answer(question_number = num-1, answer = answer)
        new_answer.save()
        ques = question_list[num-1]
        num += 1

    context = {'number' : num, 'question' : ques}
    return render(request, 'mbti/question.html', context)



def printResult(request):

    calc.questionCalc()
    artist_list = calc.estimateArtist()
    print("artist_list", artist_list)

    randomIdx = random.randrange(0,len(artist_list))
    artist = artist_list[randomIdx]

    isExistArtist = Artist.objects.filter(artist=artist)
    if (len(isExistArtist) == 0) :
        print("new Artist")
        makeSongs(artist)

    #Answer 삭제
    answer_all = Answer.objects.all()
    answer_all.delete()

    song_all = Song.objects.filter(artist = artist)

    content = {'match_artist': artist, 'song_list' : song_all}
    return render(request, 'mbti/result.html', content)


def makeSongs(artist):
    #chrome 띄우지 않고 백그라운드에서 selenium 크롤링
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

    driver = webdriver.Chrome('C:/Users/q/Desktop/chromedriver.exe', chrome_options=chrome_options)
    url = "https://www.youtube.com/results?search_query="
    url += artist+"+mv"+"&sp=EgIQAQ%253D%253D"
    driver.get(url)
    
    page = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page, 'lxml')
    all_crawl = soup.find_all('ytd-video-renderer', 'style-scope ytd-item-section-renderer')
    success = 0
    i = 0
    while (success < 4) : 
        try:
            ##print(i)
            song_url = "https://www.youtube.com/embed/"
            image = all_crawl[i].find('div').find('ytd-thumbnail').find('a')
            url = image.attrs['href']
            url_idx = url.index('=')
            song_url += url[url_idx+1:]
            song_thumbnail = image.find('yt-img-shadow', 'style-scope ytd-thumbnail no-transition').find('img').attrs['src']
            song_title = all_crawl[i].find('div').find('div','text-wrapper').find('div', 'style-scope ytd-video-renderer').find('div', 'style-scope ytd-video-renderer').find('h3').find('a').find('yt-formatted-string', 'style-scope ytd-video-renderer').get_text()
            success += 1
            i += 1
            print(song_url, song_thumbnail, song_title)
            ### 노래 db에 추가 ###
            new_song = Song(artist = artist, url = song_url, title = song_title, thumbnail = song_thumbnail, idx = success)
            new_song.save()
        except:
            #print("ERROR")
            i += 1
    new_artist = Artist(artist = artist)
    new_artist.save()



    