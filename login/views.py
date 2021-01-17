from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'login/login.html')

def checkLogin(request):
    userID = request.GET['userID']
    userPW = request.GET['userPW']

    if (userID=="") :
        content = {'announce' : "ID를 입력해주세요."}
        return render(request, 'login/loginmodal.html', content)
    elif (userPW==""):
        content = {'announce' : "비밀번호를 입력해주세요."}
        return render(request, 'login/loginmodal.html', content)

    checkUser = User.objects.filter(userID = userID)
    if (len(checkUser) == 0) :
        content = {'announce' : "존재하지 않는 user입니다."}
        return render(request, 'login/loginmodal.html', content)

    sameID = checkUser[0]
    if (sameID.userPW == userPW) :
        #쿠키 남기기
        #홈으로 이동하도록 하기
        request.session['userID']=userID
        return redirect('/home/')
    else:
        content = {'announce' : "비밀번호가 틀렸습니다."}
        return render(request, 'login/loginmodal.html', content)

def signup(request):
    return render(request, 'login/signup.html')

def checkSignup(request):
    userID = request.GET['userID']
    userPW = request.GET['userPW']
    if (len(User.objects.filter(userID = userID)) == 0):
        newUser = User(userID = userID, userPW = userPW, mbti="")
        newUser.save()
        return render(request, 'login/login.html')
    else:
        return render(request, 'login/signupmodal.html')

def modal(request):
    return render(request, 'login/modal.html')