from django.contrib import admin
from django.urls import path
from .views import inicio, cursos, nosotros, contacto, entrada, register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('login/', LoginView.as_view( template_name= 'diseño/accounts/login.html'), name= 'login' ),
    path('register/', register, name= 'register'),
    path('logout/', LogoutView.as_view(), name= 'logout' ),
    path('index.html', inicio),
    path('nosotros.html', nosotros, name='Nosotros'),
    path('contacto.html', contacto, name= 'Contacto'),
    path('cursos.html', cursos, name='Cursos'),
    path('entrada.html', entrada),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
