from django.shortcuts import render
from django.shortcuts import redirect
from login.models import *
from mbti.calc import *
import ast
from .models import *

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
            print(estimateArtistOnly(user.mbti))

            settingPersona(user, True)

            content = {'userName':userName, 'mbti': mbti}
            return render(request, 'home/home_mbti.html', content)
        except:
            if (user.mbti != ""):
                # 이미 mbti 결과가 있는 경우
                # mbti setting
                mbti = ast.literal_eval(user.mbti)

                settingPersona(user, False)

                content = {'userName':userName, 'mbti' : mbti}
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
        if (resetMbti):
            #artist 목록 추가
            persona = Persona.objects.filter(userID = userID)[0]
            persona.mbti = user.mbti
            origin_artist_list = ast.literal_eval(persona.artist)
            origin_artist_list.append(estimateArtistOnly(user.mbti))
            origin_artist_list = list(set(origin_artist_list))
            persona.artist = origin_artist_list
            persona.save()
    else:
        mbti = user.mbti
        artist = estimateArtistOnly(mbti)
        new_persona = Persona(userID = userID, mbti = mbti, artist = artist, songs = "[]", grade = "[]")
        new_persona.save()
