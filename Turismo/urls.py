from django.urls import path 
from Turismo import views
    
urlpatterns = [
    path('destino/', views.destino, name="Destinos"),
    path('profesionales/', views.profesionales, name="Profesionales"),
    path('usuario/', views.usuario, name="Usuario"),
    path('', views.inicio, name="Inicio"),
    path('consultas/', views.consultas, name="Consultas"),
    path('listaProfes/', views.listaProfesionales, name="ListaProfesionales"),
    path('borrarProfes/<profesional_nombre>', views.borrarProfresionales, name="BorrarProfes"),
    path('editarProfes/<profesional_nombre>', views.editarProfesionales, name="EditarProfes"),


    

]