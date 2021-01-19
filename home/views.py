from django.shortcuts import render
from django.shortcuts import redirect
from login.models import *
from mbti.calc import *
import ast
from .models import *
from mbti.models import *
from mbti.views import *
import simplejson as json


# Create your views here.
def index(request):
    userName = request.session.get('userName')
    if userName:
        user = User.objects.filter(userName = userName)[0]
        try:
            # 방금 검사 결과 받아온 경우
            # mbti setting
            mbti = request.GET['mbti_result']
            mbti = ast.literal_eval(mbti)
            user.mbti = mbti
            user.save()

            persona = settingPersona(user, True)
            song_list = settingSongList(persona.artist)

            content = {'userName':userName, 'mbti': mbti, 'artist_list':persona.artist, 'song_list':song_list}
            return render(request, 'home/home_mbti.html', content)
        except:
            if (user.mbti != ""):
                # 이미 mbti 결과가 있는 경우
                # mbti setting
                mbti = user.mbti
                if (type(mbti)==str):
                    mbti = ast.literal_eval(mbti)

                persona = settingPersona(user, False)

                artist = persona.artist
                if (type(artist) == str):
                    artist = ast.literal_eval(artist)
                song_list = settingSongList(artist)

                content = {'userName':userName, 'mbti' : mbti, 'artist_list':artist, 'song_list': song_list}
                return render(request, 'home/home_mbti.html', content)
            else:
                # 아직 mbti 결과가 없는 경우
                content = {'userName':userName}
                return render(request, 'home/home_nombti.html', content)

    else:
        return redirect('/login/')

def settingPersona(user, resetMbti):
    #persona setting하기
    userID = user.userID
    if (len(Persona.objects.filter(userID = userID))!= 0):
        #이미 persona 존재
        persona = Persona.objects.filter(userID = userID)[0]
        if (resetMbti):
            #artist 목록 추가
            persona.mbti = user.mbti
            origin_artist_list = persona.artist
            if (type(origin_artist_list) == str) :
                origin_artist_list = ast.literal_eval(origin_artist_list)
            origin_artist_list += estimateArtistOnly(user.mbti)
            artist_list = list(set(origin_artist_list))
            persona.artist = artist_list
            persona.save()
            return persona
        return persona
    else:
        mbti = user.mbti
        if (type(mbti) == str) :
            mbti = ast.literal_eval(mbti)
        
        artist = estimateArtistOnly(mbti)
        new_persona = Persona(userID = userID, mbti = mbti, artist = artist, songs = "[]", grade = "[]")
        new_persona.save()
        return new_persona

def settingSongList(artist_list):
    result_list = []
    for artist in artist_list:
        result = []
        song_list = Song.objects.filter(artist = artist)
        if (len(song_list) == 0):
            makeSongs(artist)
        song_list = Song.objects.filter(artist = artist)
        for song in song_list:
            result.append(song)
        result_list.append(result)
    return result_list

def matchingTogether(request, other):
    userName = request.session.get('userName')
    otherUser = User.objects.filter(userID = other)
    if (len(otherUser) == 0) :
        resultMessage = other + "라는 ID의 회원이 존재하지 않습니다."
        result = [False, resultMessage]
        return result
    otherPersona = Persona.objects.filter(userID = other)
    if (len(otherPersona) == 0) :
        resultMessage = other + "님께서 성향검사를 하지 않으셨습니다."
        result = [False, resultMessage]
        return result
    else:
        others = otherPersona[0]
        userID = User.objects.filter(userName = userName)[0].userID
        users = Persona.objects.filter(userID = userID)[0]
        users_artist = users.artist
        others_artist = others.artist
        if (type(users_artist) == str) :
            users_artist = ast.literal_eval(users_artist)
        if (type(others_artist) == str) :
            others_artist = ast.literal_eval(others_artist)
        intersection = set(users_artist) & set(others_artist)
        intersection = list(intersection)
        result = [True, intersection]
        return result

def sharedMusic(request):
    userName = request.session.get('userName')
    otherUserID = request.GET.get('id')
    result = matchingTogether(request, otherUserID)
    if (result[0]):
        content = {'intersection':result[1], 'other':otherUserID, 'user':userName}
        return HttpResponse(json.dumps(content), content_type="application/json")
    else:
        content = {'errorMessage':result[1]}
        return HttpResponse(json.dumps(content), content_type="application/json")

def goodSong(request):
    userName = request.session.get('userName')
    song_url = request.GET.get('song')
    good_song = Song.objects.filter(url = song_url)[0]
    userID = User.objects.filter(userName = userName)[0].userID
    userPersona = Persona.objects.filter(userID = userID)[0]
    good_song_list = userPersona.songs
    if (type(good_song_list) == str) :
        good_song_list = ast.literal_eval(good_song_list)
    good_song_list.append(good_song.title)
    userPersona.songs = good_song_list
    userPersona.save()
    content = {'success':True}
    return HttpResponse(json.dumps(content), content_type="application/json")

def checkGoodSong(request):
    userName = request.session.get('userName')
    song_url = request.GET.get('song')
    good_song = Song.objects.filter(url = song_url)[0]
    good_song_title = good_song.title
    userID = User.objects.filter(userName = userName)[0].userID
    userPersona = Persona.objects.filter(userID = userID)[0]
    good_song_list = userPersona.songs
    if (type(good_song_list) == str) :
        good_song_list = ast.literal_eval(good_song_list)
    if (good_song_title in good_song_list) :
        content = {'check':True}
        return HttpResponse(json.dumps(content), content_type="application/json")
    else :
        content = {'check':True}
        return HttpResponse(json.dumps(content), content_type="application/json")

def playlist(request):
    userName = request.session.get('userName')
    userID = User.objects.filter(userName = userName)[0].userID
    playlist = Persona.objects.filter(userID = userID)[0].songs
    if (type(playlist) == str) :
        playlist = ast.literal_eval(playlist)

    urlList = ""
    for title in playlist:
        url = Song.objects.filter(title=title)[0].url
        idx = url.index("embed/")
        token = url[idx+6:]
        urlList += token + ","
    urlList = urlList[:-1]
    content = {'playlist':urlList}
    return render(request, 'home/playlist.html', content)

def deleteArtist(request):
    userName = request.session.get('userName')
    userID = User.objects.filter(userName = userName)[0].userID
    persona = Persona.objects.filter(userID = userID)[0]
    artistList = persona.artist
    if (type(artistList) == str) :
        artistList = ast.literal_eval(artistList)

    artist = request.GET.get('artist')
    artistList.remove(artist)
    persona.artist = artistList
    persona.save()
    content = {'success':True}
    return HttpResponse(json.dumps(content), content_type="application/json")

