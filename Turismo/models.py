from mailbox import NoSuchMailboxError
from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40, default="")

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
        return f" id: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido}, - Email: {self.email} - Cargo: {self.cargo}"
    class Meta: 
        verbose_name_plural = "Profesionales"

class Consultas(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    consulta = models.TextField(default="")

    def __str__(self):
        txt = "{0} , {1}"
        return txt.format(self.nombre, self.apellido)
    class Meta: 
        verbose_name_plural = "Consultas"



    