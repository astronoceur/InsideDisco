from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Artista(models.Model):
    nome = models.CharField(max_length=150)
    def __str__(self):
       return self.nome

class Genero(models.Model):
    nome      = models.CharField(max_length=150)
    descricao = models.TextField()

    def __str__(self) -> str:
        return f'{self.nome}'

class Album(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.IntegerField()
    genero = models.ManyToManyField(Genero,blank=True)
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="post-img")

    def get_absolute_url(self):
        return reverse('titulo', dic={'chave': self.pk})

    def __str__(self) -> str:
        return f'{self.titulo}'

