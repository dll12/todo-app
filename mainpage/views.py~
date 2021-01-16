from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import todoform
from .models import todo
from django.utils import timezone

def mainpage(request):
    return render(request,'mainpage/mainpage.html')

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

def createtodo(request):
    if request.method == 'GET':
        return render(request,'mainpage/createtodo.html',{'form':todoform()})
    else:
        try:
            form = todoform(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('home')
        except ValueError:
            return render(request,'mainpage/createtodo.html',{'form':todoform(),'error':'The Input Limit exceeded. Try Again.'})


def home(request):
    todos = todo.objects.filter(user = request.user, datecompleted__isnull=True).order_by('-created')
    return render(request, 'mainpage/home.html',{'todos':todos})

def viewtodo(request, todo_id):
    obj = get_object_or_404(todo, pk=todo_id, user=request.user)
    form = todoform(instance=obj)
    if request.method == "GET":
        return render(request, 'mainpage/viewtodo.html',{'todo':obj,'form':form})
    else:
        try:
            form1 = todoform(request.POST,instance = obj)
            form1.save()
            return redirect('home')

        except ValueError:
            return render(request, 'mainpage/viewtodo.html',{'todo':obj,'form':form,'error':'The Input Limit exceeded.Try Again.'})

def completetodo(request, todo_id):
    if request.method == "POST":
        form = get_object_or_404(todo, pk=todo_id, user=request.user)
        form.datecompleted = timezone.now()
        form.save()
        return redirect('home')


def removetodo(request, todo_id):
    if request.method == "POST":
        form = get_object_or_404(todo, pk=todo_id, user=request.user)
        form.delete()
        return redirect('home')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('mainpage')

def loginuser(request):
    if request.method == "GET":
        return render(request,'mainpage/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'mainpage/loginuser.html',{'form':AuthenticationForm(),'error':'The Username or the Password is Incorrect! '})
        else:
            login(request,user)
            return redirect('home')




