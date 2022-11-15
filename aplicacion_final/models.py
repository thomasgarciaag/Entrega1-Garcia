from django.db import models

# Create your models here.

class contacto(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()

class sugerencia(models.Model):
    nombre = models.CharField(max_length=20)
    sugerencia = models.CharField(max_length=200)

class email(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()

    
