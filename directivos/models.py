from django.db import models

# Create your models here.

class directivos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)