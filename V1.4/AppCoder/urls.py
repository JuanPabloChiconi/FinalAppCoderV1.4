from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    

    
    path('sensores', views.agregarSensores, name="Sensores"),
    path('usuarios', views.agregarUsuario, name="Usuarios"),
    path('datospersonales', views.agregarDatosPersonales, name="DatosPersonales"),
    path('eliminarsensor/<sensor_identificacion>/', views.eliminarSensor, name="eliminarSensor"),
    path('leerSensores', views.leerSensores, name="leerSensores"),
    path('buscar/', views.buscar),
    path('editarSensor/<sensor_identificacion>/', views.editarSensor, name="editarSensor"),

    path('eliminarusuarios/<usuario_nombre>/', views.eliminarUsuario, name="eliminarUsuario"),
    path('leerUsuarios', views.leerUsuarios, name="leerUsuarios"),
    path('editarUsuario/<usuario_nombre>/', views.editarUsuario, name="editarUsuario"),

    path('eliminarDatosPersonales/<datospersonales_nombre>/', views.eliminarDatosPersonales, name="eliminarDatosPersonales"),
    path('leerDatosPersonales', views.leerDatosPersonales, name="leerDatosPersonales"),
    path('editarDatosPersonales/<datospersonales_nombre>/', views.editarDatosPersonales, name="editarDatosPersonales"),
   

    path('acercademi', views.Acercademi, name="Acercademi"),

    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    
    

    
    #path(r'^editar/(?P<pk>\d+)$', views.DatosPersonalesUpdate.as_view(), name='Edit'),
    #path(r'^refrescar/(?P<pk>\d+)$', views.DatosPersonalesDetalle.as_view(), name='Refrescar'),
    
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),

    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),

    

]

