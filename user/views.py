from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *


from user.forms import SignUpForm
# Create your views here.

def user(request):
    return HttpResponse("this is user page")


def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            current_user=request.user
            userprofile=UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage']=userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,'invalid username or password')
            return HttpResponseRedirect('/login/')
    return render(request,'login.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        check_user=User.objects.filter(username=username)
        try:
            if username not in check_user:
                if password1 == password2:
                    User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                             password=password1)

                    user = authenticate(username=username, password=password1)
                    login(request, user)
                    current_user = request.user
                    data = UserProfile()
                    data.user_id = current_user.id
                    data.image = "images/default_pic.png"
                    data.save()
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, 'password does not match')
            else:
                messages.warning(request, 'username already taken')
        except:
            messages.warning(request,'username already taken')



    return render(request,'signup.html')