from django.shortcuts import render
from django.shortcuts import redirect
from login.models import *
from mbti.calc import *
import ast
from .models import *
from mbti.models import *

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
        for song in song_list:
            result.append(song)
        result_list.append(result)
    return result_list
