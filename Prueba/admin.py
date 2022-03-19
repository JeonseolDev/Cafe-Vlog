from django.contrib import admin
from Prueba.models import Usuario, Curso, Order, Producto

# Register your models here.

admin.site.register(Curso)
admin.site.register(Order)
admin.site.register(Producto)
admin.site.register(Usuario)