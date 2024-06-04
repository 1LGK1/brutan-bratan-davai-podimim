from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment , Blog , Videos , Feedback
from django.db import models

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"})
    )

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Подтвердите пароль"})
    )

    class Meta:
        model = User
        fields = ("username", "email","password1", "password2")

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text' : "Комментарий"} 

class MakePost (forms.ModelForm):
    posted = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Blog
        fields = ('title','description','content','image','posted')

class MakeVideo(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ('name','video_file')



class Feedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('username','city','content','feedback')