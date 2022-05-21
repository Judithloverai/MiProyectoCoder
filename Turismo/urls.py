from django.urls import path, re_path
from Turismo import views
from django.contrib.auth.views import LogoutView
    
urlpatterns = [
    path('destino/', views.destino, name="Destinos"),
    path('profesionales/', views.profesionales, name="Profesionales"),
    path('cliente/', views.cliente, name="Cliente"),
    path('', views.inicio, name="Inicio"),
    path('consultas/', views.consultas, name="Consultas"),
    path('listaProfes/', views.listaProfesionales, name="ListaProfesionales"),
    path('borrarProfes/<profesional_nombre>', views.borrarProfresionales, name="BorrarProfes"),
    path('editarProfes/<profesional_nombre>', views.editarProfesionales, name="EditarProfes"),
    path('editarUsuario', views.editarUsuario, name="EditarUsuario"),


    path('consultas/lista', views.ConsultasList.as_view(), name ="ListConsultas"),
   
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='Turismo/logout.html'), name='Logout'),
    path('Registrar', views.register, name='Registrar'),


]