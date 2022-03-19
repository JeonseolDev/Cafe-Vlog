from django.db import models
# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"

class Registrarse_Curso(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    curso = models.CharField(max_length=20)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data = models.CharField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    nombre = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    

class Producto(models.Model):
    CATEGORY = (('Indoor', 'Indoor'),
               ('Out Door', 'Out Door'))

    nombre = models.CharField(max_length=200, null=True)
    precio = models.Float.Field(null=True)
    categoria = models.CharField(max_length=200, null=True, choices= CATEGORY)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(tag)

class Order(models.Model):
    STATUS = (('Pending', 'Pending'),
             ('Out of delivery', 'Out of delivery'),
             ('Delivered', 'Delivered'))

    comprador = models.ForeignKey(Customer, null= True, on_delete= models.SET_NULL)
    producto = models.ForeignKey(Product, null = True, on_delete= models.SET_NULL)
    data_creada = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_lenght=200, null=True, choices=STATUS)