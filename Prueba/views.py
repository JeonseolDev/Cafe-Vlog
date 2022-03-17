from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Login
from Prueba.forms import CreateUser
from django.contrib import messages

def inicio(request):
    return render(request, "templates/diseño/index.html", {})

def cursos(request):
    return render(request, "templates/diseño/cursos.html", {})

def nosotros(request):
    return render(request, "templates/diseño/nosotros.html", {})
    
def contacto(request):
    return render(request, "templates/diseño/contacto.html", {})
    
def entrada(request):
    return render(request, "templates/diseño/entrada.html", {})

# def login(request):
#     form = CreateUserForm()
    
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('login')
#     context = {'form':form}
#     return render(request, 'accounts/login.html', context)

def register(request):
    if request.method == 'POST':
        f = CreateUser(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = CreateUser()

    return render(request, 'diseño/accounts/register.html', {'form': f})
# def formulario_curso(request):
#     if request.method == 'POST':
#         formulario = LoginFormulario(request.POST)

#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             nuevo_user = Login(nombre=data['nombre'], contraseña=data['contraseña'])
#             nuevo_user.save()
#     formulario = LoginFormulario()
#     return render(request, 'diseño/formulario_login',{'formuilario': formulario})
    
# def busqueda_login(request):
#     buscador = LoginBusqueda()
