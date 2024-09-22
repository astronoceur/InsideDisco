import http
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from site_layout.urls import home

# Create your views here.

def login(request):
    nome = request.POST.get('username')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=nome, password=senha)
    if user is not None:
        auth.login(request,user)
        print('login ok')
        return redirect(home)
    return render(request, 'site_open/login.html')

def registro(request):
    if request.method == 'GET':
        return  render(request, 'site_open/reg.html')
    else: 
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        print(f"{nome},{email},{senha}")        

        user = User.objects.filter(username=nome)

        if user:
            print(f'{nome} já existe')
            return render(request, 'site_open/reg.html')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
    
        return render(request, 'site_open/login.html')