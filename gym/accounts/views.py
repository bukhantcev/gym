from lib2to3.fixes.fix_input import context

from django.contrib.auth import login, authenticate, logout
from django.db.transaction import commit

from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('calendar')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def registration(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.username = user.username.lower()
            context = {
                'username': user.username,
            }
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)

            return render(request, 'main/welkom.html', context=context)
        else:
            messages.success(request, 'You have singed up successfully.')
            return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)

    return redirect('login')



