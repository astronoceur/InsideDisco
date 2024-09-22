from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from site_disco.models import *

# Create your views here.
  

def disco1(request,id):
    dados = Album.objects.get(id=id)
    dic = {'album':dados}    
    return render(request,'site_disco/disco1.html',dic)
    
def get_absolute_url(self):
    pass
    
