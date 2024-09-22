from django.urls import path
from site_open.views import *

urlpatterns = [
    path('',login,name='login'),
    path('reg/', registro, name='registro'),
]