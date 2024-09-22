from django.urls import path
from site_disco.views import *
from site_layout.views import *

urlpatterns = [
    path('pag2/<int:id>', disco1, name='disco1'),
]