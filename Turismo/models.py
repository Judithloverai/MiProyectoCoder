from mailbox import NoSuchMailboxError
from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format(self.nombre, self.ubicacion)

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        txt = "{0} , {1}"
        return txt.format(self.nombre, self.apellido)

class Profesionales(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    cargo = models.CharField(max_length=40, default="")

    def __str__(self):
        txt = "{0} , {1}"
        return txt.format(self.nombre, self.apellido)
    class Meta: 
        verbose_name_plural = "Profesionales"

class Consultas(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        txt = "{0} , {1}"
        return txt.format(self.nombre, self.apellido)
    class Meta: 
        verbose_name_plural = "Consultas"



    