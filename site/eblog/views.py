from django.shortcuts import render , redirect 
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm , CommentForm
import datetime
from django.http import HttpRequest
from django.urls import reverse
from .models import Blog , Comment
from django.contrib.auth import logout

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

    """Renders the blog page."""

    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    context = {
    'title':'Блог',
    'posts': posts, 
    }


    return render(request,'blogs.html',context)

def blogpost(request, parametr):

    assert isinstance(request, HttpRequest)

    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    if request.method == "POST": # после отправки данных формы на сервер методом POST

        form = CommentForm(request.POST)

        if form.is_valid():

            comment_f = form.save(commit=False)

            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя

            comment_f.date = datetime.datetime.now() # добавляем в модель Комментария (Comment) текущую дату

            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий

            comment_f.save() # сохраняем изменения после добавления полей

            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

    else:

        form = CommentForm() # создание формы для ввода комментария
        
    context = {
        'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
        'comments': comments, 
        'form':form,
        

    }
    return render(request,'blogpost.html',context)


def logout_view(request):
    logout(request)
    return redirect('login')


def makepost(request):
    return render(request,"makepost.html")