from django.http import HttpResponse
from django.shortcuts import render
from Turismo.forms import ConsultaFormulario, ProfesionalesFormulario
from Turismo.models import Consultas, Profesionales


def destino(request):

    return render(request,"Turismo/destino.html")



def profesionales(request):

    if request.method == 'POST':

        miFormulario = ProfesionalesFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data 

            profesional = Profesionales(nombre=informacion["nombre"],
                                        apellido=informacion["apellido"],
                                        email=informacion["email"],
                                        cargo=informacion["cargo"],)
            profesional.save()
            return render(request,"Turismo/inicio.html")

    else:

        miFormulario = ProfesionalesFormulario()
    dict1={"miForm":miFormulario}    
    return render(request,"Turismo/profesionales.html", dict1)


    
def usuario(request):
     return render(request,"Turismo/usuario.html")


def inicio (request):

    return render(request,"Turismo/inicio.html")

def consultas (request):

    if request.method == 'POST':
        miFormulario = ConsultaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

        consultas = Consultas( 
            consulta=informacion['consulta'], 
            nombre=informacion['nombre'], 
            apellido=informacion['apellido'],
            email=informacion['email'],)
        consultas.save()

        return render(request, "Turismo/inicio.html")
    else:
        miFormulario = ConsultaFormulario()
    
    dict1={"miFormulario": miFormulario}
    return render(request, "Turismo/consultas.html", dict1)

def listaProfesionales(request):

        profesionales = Profesionales.objects.all()
    
        contexto = {"profesionales":profesionales}

        return render(request, "Turismo/leerProfesionales.html",contexto)

def borrarProfresionales(request, profesional_nombre):

    profesionales = Profesionales.objects.get(nombre = profesional_nombre)

    profesionales.delete()

    profesionales = Profesionales.objects.all()

    contexto={"profesionales":profesionales}

    return render(request, "Turismo/leerProfesionales.html", contexto)

def editarProfesionales(request, profesional_nombre):
    
    profesionales = Profesionales.objects.get(nombre = profesional_nombre)

    if request.method == "POST":
        miFormulario = ProfesionalesFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesionales.nombre = informacion['nombre']
            profesionales.apellido = informacion['apellido']
            profesionales.email = informacion['email']
            profesionales.cargo = informacion['cargo']

            profesionales.save()

        return render(request, "Turismo/inicio.html")

    else:

            miFormulario = ProfesionalesFormulario(initial={'nombre':profesionales.nombre, 'apellido':profesionales.apellido,
                                                        'email':profesionales.email,'cargo':profesionales.cargo })
    
    return render(request,"Turismo/editarProfesionales.html", {'miFormulario':miFormulario, 'profesional_nombre':profesional_nombre})






