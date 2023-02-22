from gettext import npgettext
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# import numpy as np
import os
import glob


def home(request):
    return render(request, "authentification/index.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('plagia')
        else:
            return HttpResponse('Votre nom ou Votre mot est incorrect veuillez vous inscrir ')
    return render(request, "authentification/signin.html")


def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if pass1 != confirm:
            return HttpResponse("votre mot de passe n'est pas le meme corriger le")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('signin')
    return render(request, "authentification/signup.html")


def signout(request):
    return render(request, "authentification/signout.html")


def plagia(request):
    # efining a function to compare the strings using levenshtein's algorithm

    return render(request, 'authentification/plagia.html')
