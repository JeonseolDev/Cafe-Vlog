from django.contrib import admin
from django.urls import path

from Cafe.settings import LOGIN_REDIRECT_URL
from .views import borrar_compra, borrar_curso, configuracion, crear_compra, crear_curso, curso, modificar_compra, modificar_curso, user_page, usuario, inicio, sobremi, contacto, entrada, register_view, login_view, logout_view, view_usuarios
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', inicio, name= 'inicio'),

    path('login/', login_view, name= 'login' ),
    path('register/', register_view, name= 'register'),
    path('logout/', logout_view, name= 'logout' ),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="diseño/accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="diseño/accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="diseño/accounts/password_reset_complete.html"), name="password_reset_complete"),

    path('index/', inicio),
    path('about/', sobremi, name='Sobremi'),
    path('contacto/', contacto, name= 'Contacto'),
    path("cursos/", curso, name="Cursos"),
    path('entrada/', entrada, name="entrada"),
    
    path('usuario/', view_usuarios, name="usuarios"),
    path('usuario/<str:pk_test>/', usuario, name="usuario"),
    path("user/", user_page, name="user"),
    path("configuracion/", configuracion, name="configuracion"),

    path('configurar_cursos/', crear_curso, name='productos'),
    path('modificar_curso/<str:pk>/', modificar_curso, name="modificar_curso"),
    path('borrar_curso/<str:pk>/', borrar_curso, name="borrar_curso"),

    path('comprar_cursos/', crear_compra, name='crear_compra'),
    path('modificar_compra/<str:pk>/', modificar_compra, name="modificar_compra"),
    path('borrar_compra/<str:pk>/', borrar_compra, name="borrar_compra"),

    path('admin/', admin.site.urls),
    
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
