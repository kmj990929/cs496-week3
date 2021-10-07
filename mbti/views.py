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
from pyvirtualdisplay import Display
from . import calc
import random
import ast



def index(request):
    userName = request.session.get('userName')
    if userName:
        content = {'status' : "Logout"}
    else:
        content = {'status' : "Login"}
    return render(request, 'mbti/index.html', content)



def printQuestion(request, quesNum):
    num = int(quesNum)
    question_list = [
        "나는 남의 시선을 신경쓰는 편이다.",
        "나는 공무원을 꿈으로 가지는 것이 바람직하지 않다고 생각한다.",
        "나는 내가 백만장자가 될 수 있을 것이라고 생각한다.",
        "나는 많은 사람들과 어울리는 것이 어렵게 느껴진다.",
        "나는 남보다 화를 잘 참는 편이다.",
        "나는 평소에 조급하거나 불안한 감정을 자주 느끼는 편이다.",
        "나는 휴일에 다른 사람이 깨우기 전에 침대에서 일어나지 않는 편이다.",
        "나는 회식에 참여하는 것보다 집에서 쉬는 것을 선호하는 편이다.",
        "나는 종종 혼자 밤산책을 즐긴다.",
        "나는 친구가 고민을 말할 때 속으로 잘잘못을 따진다."]

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

    userName = request.session.get('userName')
    if userName:
        context = {'number' : num, 'question' : ques, 'status' : "Logout"}
    else:
        context = {'number' : num, 'question' : ques, 'status' : "Login"}
    return render(request, 'mbti/question.html', context)



def printResult(request):
    calc.questionCalc()
    estimate = calc.estimateArtist()
    artist_list = estimate[0]
    mbti_list = estimate[1]
    print("artist_list", artist_list)
    print("mbti_list", mbti_list)
    
    profile_list = []
    for person in artist_list:
        if (len(Artist.objects.filter(artist=person)) == 0):
            profile = getProfileImage(person)
            new_artist = Artist(artist = person, profile_image = profile)
            new_artist.save()
        profile_list.append(Artist.objects.filter(artist=person)[0])

    randomIdx = random.randrange(0,len(artist_list))
    artist = artist_list[randomIdx]

    isExistArtist = Song.objects.filter(artist=artist)
    if (len(isExistArtist) == 0) :
        print("new Artist")
        makeSongs(artist)

    song_all = Song.objects.filter(artist = artist)

    userName = request.session.get('userName')
    if userName:
        content = {'match_artist': artist, 'song_list' : song_all, 'profile_list' : profile_list, 'artist_list_string' : artist_list, "mbti_list": mbti_list, 'status' : "Logout"}
    else:
        content = {'match_artist': artist, 'song_list' : song_all, 'profile_list' : profile_list, 'artist_list_string' : artist_list, "mbti_list": mbti_list, 'status' : "Login"}

    return render(request, 'mbti/result.html', content)



def printMatching(request, matching):
    #song 만들기
    isExistArtist = Song.objects.filter(artist=matching)
    if (len(isExistArtist) == 0) :
        print("new Artist")
        makeSongs(matching)
    song_all = Song.objects.filter(artist = matching) 

    #profile 만들기
    artist_list = request.GET['artist_list_string']
    artist_list = ast.literal_eval(artist_list)
    artist_idx = artist_list.index(matching)
    artist_list = artist_list[artist_idx:] + artist_list[:artist_idx]
    profile_list = []
    for person in artist_list:
        profile_list.append(Artist.objects.filter(artist=person)[0])

    mbti_list = request.GET['mbti_list_string']
    mbti_list = ast.literal_eval(mbti_list)

    userName = request.session.get('userName')
    if userName:
        content = {'match_artist': matching, 'song_list' : song_all, 'profile_list' : profile_list, 'artist_list_string' : artist_list, 'mbti_list': mbti_list, 'status' : "Logout"}
    else:
        content = {'match_artist': matching, 'song_list' : song_all, 'profile_list' : profile_list, 'artist_list_string' : artist_list, 'mbti_list': mbti_list, 'status' : "Login"}
    return render(request, 'mbti/result.html', content)



def makeSongs(artist):
    #chrome 띄우지 않고 백그라운드에서 selenium 크롤링
    url = "https://www.youtube.com/results?search_query="
    url += artist+"+mv"+"&sp=EgIQAQ%253D%253D"
    driver = getUrl(url)
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

def getUrl(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

    #display = Display(visible=0, size = (1920, 1080))
    #display.start()
    #driver = webdriver.Chrome('/home/ubuntu/cs496-week3/chromedriver', chrome_options=chrome_options)
    driver = webdriver.Chrome('C:/Users/USER/Desktop/startup_crawling/chromedriver.exe', chrome_options=chrome_options)
    driver.get(url)
    return driver

def getProfileImage(artist):
    naverUrl = "https://www.melon.com/search/total/index.htm?q="
    naverUrl += artist + "&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&linkOrText=T&ipath=srch_form"
    naverDriver = getUrl(naverUrl)
    naverPage = naverDriver.page_source
    naverDriver.quit()
    naverSoup = BeautifulSoup(naverPage, 'lxml')
    try:
        profile_img = naverSoup.find('div', 'wrap_cntt clfix d_artist_list').find('a').find('img').attrs['src']
    except:
        print("Melon profile crawling error")
        profile_img = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw4IDQgICAgKCAgICAoICAgICxAICggKFREWFhURExMYHCggGBolGxMTITEhJSk3Li4uFx8zODMtNygtLjcBCgoKBQUFDgUFDisZExkrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAOEA4AMBIgACEQEDEQH/xAAZAAEBAQEBAQAAAAAAAAAAAAAAAQMCBAf/xAAoEAEBAAEDAwQCAQUAAAAAAAAAARECAyExQVESYXGBkbHREyIyQqH/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8A+xKigAAAAAAAAAAAAAAAAAAAAAAAAAAiooAAAAAAAAAAAAAAA7/p3GZz7OAAAAAAAAAAARUUAAAAAAAAAAAdTbt7YdzZ838AyXTour+W825O2fnl0BJjhnubeeZ1/bQB5RpvaMf3T7ZgAAAAAAAAiooAAAAAAAO9vR6rz0gGjb9XN4n7badMnSKAAAAAAAmqZljzWY4ep592Yt9wcgAAAAAAAiooAAAAAAD06JiSPPp6z5ekAAAAAAAABjv9mzLf7AyAAAAAAABFRQAAAAAAXR1ny9Lyx6oAAAAAAAAAy3+321Yb3X4gOAAAAAAAARUUAAAAAAG+3p4nu7cbNzPjh2AAAAAAAAAY9gtwDzapi2e6Fubb5oAAAAAACKigAAAAAA72bi48t3llxivVLnkAAAAAAAABxvXE+XbDe1ZuPAOAAAAAAAARUUAAAAAABdOrGOeEAeqDPZ1Z47xoAAAAACatXpmQZb2rtL06sy3PPkAAAAAAAABFRQAAAAAAAAJccx6dOr1TLzO9nr9A3AAAAYbmv1X2jve6MQAAAAAAAAAARUUAAAAAAAAB3s9fpw22J1vkGgAAAON7p9sHp1zMseYAAAAAAAAAAEVFAAAFmm3pHc2b3uP+gzG02Z3tdTbk7A87qaLez0Y9gGWnZ836jWTHAAAAAAONe3LzOK7Aee7dnbPw5sx1j1GAeUem6Jezm7UBgNbs+L+XF0WdvwDkAAAEVFAbaNrvTZ0f7Xr2aAYAAAAAAAAAAAAAAAAAAABzq0TV8+WGrT6eK9Ka9PqmAeYLMcAIsmbIjvambPaA9EmAAAAAAAAAAAAAAAAAAAAAAAAY70xc+WbbenH2xBlqabPX6AGoAAAAAAAAAKgAAAAAAAAAAAAA53P8awgA/9k="
    return profile_img





    