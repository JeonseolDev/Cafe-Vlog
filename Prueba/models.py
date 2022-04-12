from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Tag(models.Model):
    nametagmodel = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nametagmodel


class Curso(models.Model):
    
    nombre = models.CharField(max_length=20, null=True)
    camada = models.IntegerField(null=True)
    precio = models.FloatField(null=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    presentacion = RichTextField(blank=True, null=True)
    imagen = models.ImageField(null=True)

    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"
        

class Registrarse_Curso(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    curso = models.CharField(max_length=20)
    

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, blank= True,on_delete=models.CASCADE)
    cursada = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL, blank=True)
    profile_pic = models.ImageField(default="profile1.png",null= True)
    nombre = models.CharField(max_length=200, null=True,)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True)
    data_creada = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre
    


class Producto(models.Model):
    CATEGORY = (('Disponible', 'Disponible'),
               ('En curso', 'En curso'))

    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField(null=True)
    categoria = models.CharField(max_length=200, null=True, choices= CATEGORY)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    data_creada = models.DateTimeField(auto_now_add=True, null=True)
    


class Ordene(models.Model):
    ESTADOS = (
        ('Activo', 'Activo'),
        ('En curso', 'En curso')
    )

    cliente = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    cursada = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)
    fecha = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.CharField(max_length=200, null=True, choices=ESTADOS)

    def __str__(self):
        return str(f"{self.cliente} {self.cursada}")
    
