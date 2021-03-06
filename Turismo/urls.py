from django.urls import path, re_path
from Turismo import views
from django.contrib.auth.views import LogoutView

    
urlpatterns = [
    path('busquedaPais/', views.busquedaPais, name="Destinos"),
    path('profesionales/', views.profesionales, name="Profesionales"),
    path('cliente/', views.cliente, name="Cliente"),
    path('abautme/', views.sobreLaCreadora, name="Abautme"),
    path('consultas/', views.consultas, name="Consultas"),
    path('listaProfes/', views.listaProfesionales, name="ListaProfesionales"),
    path('borrarProfes/<profesional_nombre>', views.borrarProfresionales, name="BorrarProfes"),
    path('editarProfes/<profesional_nombre>', views.editarProfesionales, name="EditarProfes"),
    path('editarUsuario', views.editarUsuario, name="EditarUsuario"),
    path("busquedaPais/", views.busquedaPais, name="BusquedaPais"),
    path("resultadosBusqueda/", views.resultadosBusqueda, name="Resultados"),
    path('consultas/lista', views.ConsultasList.as_view(), name ="ListConsultas"),
    path(r'^borrar/(?P<pk>\d+)$', views.ConsultaDelete.as_view(), name='Delete'),
    path(r'^(?P<pk>\d+)$', views.ConsultaDetalle.as_view(), name='Detail'),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='Turismo/logout.html'), name='Logout'),
    path('Registrar', views.register, name='Registrar'),



]