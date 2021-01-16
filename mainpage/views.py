from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def signup(request):
    if request.method == 'GET' :
        return render(request,'mainpage/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request,'mainpage/signup.html',{'form':UserCreationForm(),'error':'Password do not match'})
        else:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'mainpage/signup.html',{'form':UserCreationForm(),'error':'Username Already Exists'})

def home(request):
    return render(request, 'mainpage/home.html')