from django.urls import path 
from Turismo import views
    
urlpatterns = [
    path('destino/', views.destino),
    path('profesionales/', views.profesionales),
    path('usuario/', views.usuario),
    path('', views.inicio),
]