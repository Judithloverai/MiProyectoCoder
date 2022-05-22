from msilib.schema import ListView
from pyexpat import model
from django.http import HttpResponse
from django.shortcuts import render
from Turismo.forms import ConsultaFormulario, ProfesionalesFormulario, RegistroFormulario
from Turismo.models import Avatar, Consultas, Destino, Profesionales
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm

def register(request):

    if request.method == 'POST':    

        form = RegistroFormulario(request.POST)   

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "Turismo/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = RegistroFormulario()   
    
    
    return render(request, "Turismo/registro.html", {'form':form})



def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')  
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)    

            if user:    

                login(request, user)   

             
                return render(request, "Turismo/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:  

    
            return render(request, "Turismo/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "Turismo/login.html", {'form':form})

    


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


    
def cliente(request):
     return render(request,"Turismo/cliente.html")

def sobreLaCreadora(request):
    return render(request, "Turismo/abautme.html" )


def inicio (request):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    imagen = avatares[0].imagen.url
    return render(request,"Turismo/inicio.html", {'url': imagen})
    
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

@login_required

def borrarProfresionales(request, profesional_nombre):

    profesionales = Profesionales.objects.get(nombre = profesional_nombre)

    profesionales.delete()

    profesionales = Profesionales.objects.all()

    contexto={"profesionales":profesionales}

    return render(request, "Turismo/leerProfesionales.html", contexto)

@login_required

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

class ConsultasList(LoginRequiredMixin, ListView):

    model = Consultas
    template_name = "Turismo/listaConsultas.html"


def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST":    

        miFormulario = RegistroFormulario(request.POST) 
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     

            
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "Turismo/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username})

    return render(request, "Turismo/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})

def busquedaPais(request):

    return render(request, "Turismo/busquedaPais.html")

def buscar(request):


    if request.GET['pais']:

        pais = request.GET['pais']      
        destino = Destino.objects.filter(pais__iexact=pais)

        return render(request, "Turismo/resultadosBusqueda.html", {"destino":destino, "pais":pais})

    else:

        respuesta="No enviaste datos."
    
    return HttpResponse(respuesta)
