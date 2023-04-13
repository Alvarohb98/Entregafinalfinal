from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    titulo_tag = models.CharField(max_length=40, default="Travel Blog!")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fechapost = models.DateField(auto_now_add=True)
    categorias = models.CharField( max_length=15, default='EEUU')


    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('articulodetalle', args=(str(self.id)))


class Categorias(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')