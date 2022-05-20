from django.urls import path 
from Turismo import views
    
urlpatterns = [
    path('destino/', views.destino, name="Destinos"),
    path('profesionales/', views.profesionales, name="Profesionales"),
    path('usuario/', views.usuario, name="Usuario"),
    path('', views.inicio, name="Inicio"),
]