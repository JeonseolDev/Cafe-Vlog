from django.contrib import admin
from Prueba.models import Usuario, Curso, Ordene, Producto, Tag

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Curso)
admin.site.register(Producto)
admin.site.register(Tag)
admin.site.register(Ordene)