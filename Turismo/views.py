from django.http import HttpResponse
from django.shortcuts import render
from Turismo.forms import ConsultaFormulario
from Turismo.models import Consultas, Destino

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

def consultaFormulario(request):

    if request.method == 'POST':
        miFormulario = ConsultaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

        consultas1 = Consultas( 
            consulta=informacion['consultas'], 
            nombre=informacion['nombre'], 
            apellido=informacion['apellido'],
            mail=informacion['mail'])
        consultas1.save()

        return render(request, "Turismo/inicio.html")
    else:
        miFormulario = ConsultaFormulario()
    
    return render(request, "Turismo/consultaFormulario.html", {"miFormulario":miFormulario})