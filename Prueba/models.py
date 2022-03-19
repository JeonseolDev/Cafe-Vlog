from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    nombre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Curso(models.Model):

    # CATEGORY = (('Preparando', 'Preparando'),
    #            ('En curso', 'En curso'))

    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()
    precio = models.FloatField(null=True)
    # categoria = models.CharField(max_length=200, null=True, choices= CATEGORY)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    # data_creada = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"

class Registrarse_Curso(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    curso = models.CharField(max_length=20)
    
class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data_creada = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    CATEGORY = (('Indoor', 'Indoor'),
               ('Out Door', 'Out Door'))

    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField(null=True)
    categoria = models.CharField(max_length=200, null=True, choices= CATEGORY)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    data_creada = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

class Order(models.Model):
    STATUS = (('Pendiente', 'Pendiente'),
             ('Fuera del curso', 'Fuera del curso'),
             ('Cursando', 'Cursando'))

    comprador = models.ForeignKey(Usuario, null= True, on_delete= models.SET_NULL)
    producto = models.ForeignKey(Curso, null = True, on_delete= models.SET_NULL)
    data_creada = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)