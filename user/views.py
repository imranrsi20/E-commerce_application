from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import *
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
    return render(request,'signup.html')