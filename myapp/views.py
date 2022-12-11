from cgitb import text
from email import message
from django.shortcuts import render,redirect
from .models import Restourant
from django.contrib.auth.models import User, auth

def index (request):
    restourant1 = Restourant
    restourant1.id = 0 
    restourant1.name = "Tasty"
    Restourant.details = "Our restourant very clear"
    return render(request, 'index.html', {'restourant': restourant1})

def components (request):
    return render(request, 'components.html')

# register

def register (request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            
            if User.objects.filter(email=email).exists():
                message.info (request, 'Email Already')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                message.info (request, 'Username Already ')
                return redirect('register')
            else:
                user = User.objects.create_user (username=username, email=email,password=password)
                user.save();
                return redirect('login')
        else:
            message.info(request, 'Password error')
            return redirect('register')
    else:
        return render(request, 'register.html')

# login 
def login (request) :
    if request.method =='POST' :
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,auth)
            return redirect
        else :
            message.info (request, 'Credintails invalid')
            return redirect ('login')
    else:   
        return render (request, 'login.html')