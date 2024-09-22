from django.urls import path
from site_layout.views import *

urlpatterns = [
    path('',home,name='home'),
    path('usu/',usuario, name='pag_usu')
]