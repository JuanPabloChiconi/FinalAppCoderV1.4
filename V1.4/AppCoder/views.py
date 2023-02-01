

# Create your views here.
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from AppCoder.forms import DatosPersonalesFormulario, SensoresFormulario, UsuarioFormulario, UserRegisterForm, UserEditForm
from AppCoder.models import DatosPersonales, Sensores, Usuario, Avatar
#parte mia

#parte mia

# Create your views here.
"""

    
"""


#parte mia
    
    
from django.views.generic.detail import DetailView

def inicio(request):

    return render(request, "AppCoder/inicio.html")
  


class DatosPersonalesDetalle(DetailView):

    model = DatosPersonales
    template_name = "AppCoder/DatosPersonales.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from django.views.generic.edit import UpdateView

class DatosPersonalesUpdate(UpdateView):

    model = DatosPersonales
    success_url = "/AppCoder/DatosPersonales.html"
    fields = ['direccion', 'telefono', 'email']

"""



from django.views.generic import ListView

class SensoresList(ListView):

    model = Sensores
    template_name = "AppCoder/Sensores_list.html"


from django.views.generic.detail import DetailView


class SensoresDetalle(DetailView):

    model = Sensores
    template_name = "AppCoder/Sensores_detalle.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CursoCreacion(CreateView):

    model = Sensores
    success_url = "/AppCoder/Sensores/list"
    fields = ['identificacion', 'modelo', 'valor']

from django.views.generic.edit import UpdateView

class SensoresUpdate(UpdateView):

    model = Sensores
    success_url = "/AppCoder/Sensores/list"
    fields = ['identificacion', 'modelo', 'valor']


from django.views.generic.edit import DeleteView
class SensoresDelete(DeleteView):

    model = Sensores
    success_url = "/AppCoder/Sensores/list"

"""





"""
def buscar(request):

      if  request.GET("modelo"):

	      #respuesta = f"Estoy buscando el modelo nro: {request.GET['modelo'] }" 
            modelo = request.GET("modelo")
            sensores = Sensores.objects.filter(modelo__icontains=modelo)

            return render(request, "AppCoder/inicio.html", {"Sensores:":sensores,"Modelo":modelo})
            

      else: 
            respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)  
"""

def buscar(request):
      modelo =request.GET["modelo"]
      if modelo != "" :
            #sensores = Sensores.objects.filter(modelo)
            #respuesta = ("Sensores:", modelo)
            
            #return HttpResponse(respuesta)
            sensores = Sensores.objects.filter(modelo__icontains=modelo)
            return render(request, "AppCoder/inicio.html", {"sensoresmodelo":sensores, "Modelo":modelo})
      else: 
            respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)




### INICIO SENSORES

def leerSensores(request):

      sensores = Sensores.objects.all() #trae todos los sensores

      contexto= {"sensores":sensores} 

      return render(request, "AppCoder/leerSensores.html",contexto)



    
def eliminarSensor(request, sensor_identificacion):

    sensor = Sensores.objects.get(identificacion=sensor_identificacion)
    sensor.delete()
    # vuelvo al menú
    sensor2 = Sensores.objects.all()  # trae todos los sensores
    contexto = {"sensores": sensor2}
    return render(request, "AppCoder/leerSensores.html", contexto)


    
 
  

###   CARGA DE DATOS DE SENSORES   


from AppCoder.forms import SensoresFormulario      
def agregarSensores(request):
      if request.method == 'POST':
            miFormulario = SensoresFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacionnueva = miFormulario.cleaned_data
                  sensoresactualizados = Sensores(identificacion=informacionnueva['identificacion'], modelo=informacionnueva['modelo'],valor=
                   informacionnueva['valor'])
                  sensoresactualizados.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= SensoresFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/sensores.html", {"miFormulario":miFormulario})
  


def editarSensor(request, sensor_identificacion):

    # Recibe el nombre del sensor que vamos a modificar
    sensor= Sensores.objects.get(identificacion=sensor_identificacion)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = SensoresFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            sensor.identificacion = informacion['identificacion']
            sensor.modelo = informacion['modelo']
            sensor.valor = informacion['valor']
    

            sensor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = SensoresFormulario(initial={'identificacion':sensor.identificacion, 'modelo':sensor.modelo,
                                                   'valor':sensor.valor})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarSensor.html", {"miFormulario": miFormulario, "identificacion": sensor_identificacion})

### FIN SENSORES

### INICIO USUARIOS

def leerUsuarios(request):

      usuarios = Usuario.objects.all() #trae todos los sensores

      contexto= {"usuarios":usuarios} 

      return render(request, "AppCoder/leerUsuarios.html",contexto)



    
def eliminarUsuario(request, usuario_nombre):

    usuarios = Usuario.objects.get(nombre=usuario_nombre)
    usuarios.delete()
    # vuelvo al menú
    usuarios2 = Usuario.objects.all()  # trae todos los sensores
    contexto = {"usuario": usuarios2}
    return render(request, "AppCoder/leerUsuarios.html", contexto)

   

###   CARGA DE DATOS DE USUARIOS      
from AppCoder.forms import UsuarioFormulario      
def agregarUsuario(request):
      if request.method == 'POST':
            miFormulario = UsuarioFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacionnueva = miFormulario.cleaned_data
                  usuariosactualizados = Usuario(nombre=informacionnueva['nombre'], apellido=informacionnueva['apellido'],dni=
                   informacionnueva['dni'])
                  usuariosactualizados.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= UsuarioFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/usuarios.html", {"miFormulario":miFormulario})
  

def editarUsuario(request, usuario_nombre):

    # Recibe el nombre del usuario que vamos a modificar
    usuario= Usuario.objects.get(nombre=usuario_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = UsuarioFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.dni = informacion['dni']
    

            usuario.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = UsuarioFormulario(initial={'nombre':usuario.nombre, 'apellido':usuario.apellido,
                                                   'dni':usuario.dni})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarUsuario.html", {"miFormulario": miFormulario, "identificacion": usuario_nombre})

### FIN USUARIOS


### INICIO DATOS PERSONALES



def leerDatosPersonales(request):

      datospersonales = DatosPersonales.objects.all() #trae todos los sensores

      contexto= {"datospersonales":datospersonales} 

      return render(request, "AppCoder/leerDatosPersonales.html",contexto)



    
def eliminarDatosPersonales(request, datospersonales_nombre):

    datospersonales = DatosPersonales.objects.get(nombre=datospersonales_nombre)
    datospersonales.delete()
    # vuelvo al menú
    datospersonales2 = DatosPersonales.objects.all()  # trae todos los datos
    contexto = {"datospersonales": datospersonales2}
    return render(request, "AppCoder/inicio.html", contexto)

  

###   CARGA DE DATOS DE USUARIOS      
from AppCoder.forms import DatosPersonalesFormulario      
def agregarDatosPersonales(request):
      if request.method == 'POST':
            miFormulario = DatosPersonalesFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacionnueva = miFormulario.cleaned_data
                  datospersonalesactualizados = DatosPersonales(nombre=informacionnueva['nombre'], direccion=informacionnueva['direccion'], telefono=informacionnueva['telefono'],email=
                   informacionnueva['email'])
                  datospersonalesactualizados.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= DatosPersonalesFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/datospersonales.html", {"miFormulario":miFormulario})
  

def editarDatosPersonales(request, datospersonales_nombre):

    # Recibe el nombre del sensor que vamos a modificar
    datospersonales= DatosPersonales.objects.get(nombre=datospersonales_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = DatosPersonalesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            datospersonales.nombre = informacion['nombre']
            datospersonales.direccion = informacion['direccion']
            datospersonales.telefono = informacion['telefono']
            datospersonales.email = informacion['email']
    

            datospersonales.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = DatosPersonalesFormulario(initial={'nombre':datospersonales.nombre,'direccion':datospersonales.direccion, 'telefono':datospersonales.telefono,
                                                   'email':datospersonales.email})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarDatosPersonales.html", {"miFormulario": miFormulario, "identificacion": datospersonales_nombre})





### FIN DATOS PERSONALES


 ###LOGIN


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})



    #### LOGIN


#### REGISTRO

from AppCoder.forms import  UserRegisterForm




def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})






### REGISTRO


###Funcion para que solo el usuario logueado vea el contenido

from django.contrib.auth.decorators import login_required


#@login_required
#def inicio(request):

#    return render(request, "AppCoder/inicio.html")
#@login_required
#def estudiantes(request):

#    return render(request, "AppCoder/estudiantes.html")

###Funcion para que solo el usuario logueado vea el contenido


# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})



#Avatar
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,"AppCoder/inicio.html", {"url":avatares[0].imagen.url})



#Acerca de mi

def Acercademi(request):
    return render(request, "AppCoder/acercademi.html")
