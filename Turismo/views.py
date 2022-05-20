from django.http import HttpResponse
from django.shortcuts import render
from Turismo.models import Destino

def destino(request):

    return render(request,"Turismo/destino.html")


def profesionales(request):

    return render(request, "Turismo/profesionales.html")

    
def usuario(request):

    return render(request,"Turismo/usuario.html")


def inicio (request):

    return render(request,"Turismo/inicio.html")

def consultas (request):

    return render(request,"Turismo/consultas.html")

def usuarioFormulario(request):
    
    return render(render, "Turismo/usuarioFormulario.html")