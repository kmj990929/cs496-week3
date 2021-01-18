from django.shortcuts import render
from django.shortcuts import redirect
from login.models import *

# Create your views here.
def index(request):
    userName = request.session.get('userName')
    if userName:
        user = User.objects.filter(userName = userName)[0]
        try:
            # 방금 검사 결과 받아온 경우
            mbti = request.GET['mbti_result']
            user.mbti = mbti
            user.save()
            content = {'userName':userName, 'mbti': user.mbti}
            return render(request, 'home/home_mbti.html', content)
        except:
            if (user.mbti != ""):
                # 이미 mbti 결과가 있는 경우
                content = {'userName':userName, 'mbti' : user.mbti}
                return render(request, 'home/home_mbti.html', content)
            else:
                # 아직 mbti 결과가 없는 경우
                content = {'userName':userName}
                return render(request, 'home/home_nombti.html', content)

    else:
        return redirect('/login/')