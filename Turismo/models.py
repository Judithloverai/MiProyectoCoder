from mailbox import NoSuchMailboxError
from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()

class Profesionales(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()


    