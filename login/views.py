from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'login/login.html')

def checkLogin(request):
    userID = request.GET['userID']
    userPW = request.GET['userPW']
    print(userID, userPW)
    return HttpResponse(userID)