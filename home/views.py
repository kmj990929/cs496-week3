from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    #request.session.clear()
    userID = request.session.get('userID')
    if userID:
        print(userID)
        return render(request, 'home/home.html')
    else:
        return redirect('/login/')