from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
    
"""   
    
    

class Usuario(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre : {self.nombre} -   Apellido : {self.apellido} -   DNI : {self.dni}"


class DatosPersonales(models.Model):
    nombre = models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    telefono= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre : {self.nombre} -Direccion : {self.direccion} -   Telefono : {self.telefono} -   email : {self.email}"
    
class Sensores(models.Model):
    identificacion= models.CharField(max_length=30)
    modelo= models.CharField(max_length=30)
    valor= models.CharField(max_length=30)

    def __str__(self):
        return f"Identificacion : {self.identificacion} -   Modelo : {self.modelo} -   Valor : {self.valor}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"