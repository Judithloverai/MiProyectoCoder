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

    path('consultas/lista', views.ConsultasList.as_view(), name ="ListConsultas"),
    re_path(r'^(?P<pk>\d+)$', views.ConsultasDetalle.as_view(), name='Detail'),
    re_path(r'^nuevo$', views.ConsultasCreacion.as_view(), name="New"),
    re_path(r'^editar/(?P<pk>\d+)$', views.ConsultasEditar.as_view(), name='Edit'),
    re_path(r'^borrar/(?P<pk>\d+)$', views.ConsultasEliminar.as_view(), name='Delete'),

    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='Turismo/logout.html'), name='Logout'),
    path('Registrar', views.register, name='Registrar'),


]