from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *

def home(r):
    data = {
        "generous":Generous.objects.all(),
        "books": Post.objects.all()
    }
    return render(r,"home.html",data)

def viewBook(r):
    data = {
        "generous": Generous.objects.all(),
        "book" : Post.objects.all()
    }
    return render(r,"views.html",data)

@login_required
def addBook(r):
    form = PostForm(r.POST or None, r.FILES or None)
    data = {
        "form":form,
        "generous":Generous.objects.all()
    }

    if r.method == "POST":
        formData = form.save(commit=False)
        formData.author = r.user
        formData.save()
        return redirect(home)
    return render(r,"insert.html",data)

def deleteBook(r):
    data = Post.objects.all()
    data.delete()
    return redirect(home)

def editBook(r):
    post = Post.objects.all()
    form = PostForm(r.POST or None,r.FILES or None,instance=post)
    data = {
        "form":form,
        "generous":Generous.objects.all()
    }

    if r.method == "POST":
        formData = form.save(commit=False)
        formData.author = r.user
        formData.save()
        return redirect(home)

    return render(r,"insert.html",data)

def signUp(r):
    form = UserCreationForm(r.POST or None)
    data = {
        "form":form
    }
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(signIn)
    return render(r,"accounts/register.html",data) 

def signIn(r):
    form = AuthenticationForm(r.POST or None)
    data = {
        "form":form
    }

    if r.method == "POST":
        username = r.POST.get("username")
        password = r.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(r,user)
            return redirect(home)
    return render(r,"accounts/login.html",data)

def filterGenerous(r,id):
    data = {
        "posts":Post.objects.filter(generous__id=id),
        "generous":Generous.objects.all()
    }
    return render(r, "home.html",data)

def searchBook(r):
    search = r.GET.get('search')
    data = {
        "posts":Post.objects.filter(title__icontains=search),
        "generous":Generous.objects.all()
    }
    return render(r, "home.html",data) 

def signOut(r):
    logout(r)
    return redirect(home)