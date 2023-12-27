from django.db import models

# Create your models here.

class empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)