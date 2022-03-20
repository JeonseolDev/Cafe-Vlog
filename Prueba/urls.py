from django.contrib import admin
from django.urls import path
from .views import usuario, createOrder, deleteOrder, inicio, cursos, nosotros, contacto, entrada, productos, register, logout_view, cursos_create, buscar, updateOrder, view_usuarios, userPage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('login/', LoginView.as_view(template_name="diseño/accounts/login.html"), name= 'login' ),
    path('register/', register, name= 'register'),
    path('logout/', logout_view, name= 'logout' ),
    path('index.html', inicio),
    path('nosotros.html', nosotros, name='Nosotros'),
    path('contacto.html', contacto, name= 'Contacto'),
    # path('cursos/', cursos, name='Cursos'),
    path("cursos/", cursos_create, name="Cursos"),
    path("buscar/", buscar, name="Cursos_buscar"),
    path('entrada.html', entrada),
    path('productos/', productos, name='productos'),
    path('usuario/', view_usuarios, name="usuarios"),
    path('usuario/<str:pk_test>/', usuario, name="usuario"),
    path("user/", userPage, name="user"),

    path('create_order/', createOrder, name="create_order"),
    path('update_order/<str:pk>/', updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', deleteOrder, name="delete_order"),
    path('admin/', admin.site.urls),
    
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
