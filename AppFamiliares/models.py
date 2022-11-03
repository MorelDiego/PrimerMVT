from django.db import models

# Create your models here.

class Madre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    cumpleaños = models.DateField()

class Padre(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    cumpleaños = models.DateField()

class Hermano(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    cumpleaños = models.DateField()