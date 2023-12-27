from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_caducidad = models.DateField()