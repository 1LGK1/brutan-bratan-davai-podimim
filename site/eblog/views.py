from django.shortcuts import render , redirect 
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm , CommentForm ,MakePost , MakeVideo , Feedback
import datetime
from django.http import HttpRequest
from django.urls import reverse
from .models import Blog , Comment , Videos
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required ,permission_required

def about(request):
    return render(request, "about.html")

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse("about"))
    else:
        form = UserLoginForm()
    context = {"form": UserLoginForm}
    return render(request, "login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "registration.html", context)


def blogs(request):
    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all()
    context = {
    'title':'Блог',
    'posts': posts, 
    }


    return render(request,'blogs.html',context)

def blogpost(request, parametr):

    assert isinstance(request, HttpRequest)

    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user 
            comment_f.date = datetime.datetime.now() 
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save() 
            return redirect('blogpost', parametr=post_1.id) 
    else:
        form = CommentForm()
    context = {
        'post_1': post_1,
        'comments': comments, 
        'form':form,}
    return render(request,'blogpost.html',context)


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@permission_required('is_superuser')
def makepost(request):
    if request.method == "POST":
        form = MakePost(request.POST, request.FILES)
        form_video = MakeVideo(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect(reverse("blogs"))
        if form_video.is_valid():
            form_video.save()
            return redirect(reverse("videos"))
    else:
        form = MakePost()
        form_video = MakeVideo()
    context = {
        'form':form,
        'form_video':form_video,

    }
    
    return render(request,"makepost.html",context)

def videos(request):
    videos = Videos.objects.all()
    context = {
    'videos': videos, 
    }
    return render(request,"videos.html",context)


def feedback(request):
    if request.method == "POST":
        form = Feedback(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("feedback"))
    else:
        form = Feedback()
    context = {
        'form':form,
    }
    return render(request,"feedback.html",context)

def contacts(request):
    return render(request,"contacts.html")