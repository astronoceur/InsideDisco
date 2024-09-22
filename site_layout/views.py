from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from site_disco.models import *

# Create your views here.

def home(request):
    dados = Album.objects.all()
    dic = {'album':dados}   
    return render(request, 'site_layout/index.html',dic)

def usuario(request):
    return render(request, 'site_layout/usuario.html')