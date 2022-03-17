from django.db import models

# Create your models here.
class Login(models.Model):

    nombre = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=20)