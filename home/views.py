from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    #request.session.clear()
    userName = request.session.get('userName')
    if userName:
        content = {'userName':userName}
        return render(request, 'home/home.html', content)
    else:
        return redirect('/login/')