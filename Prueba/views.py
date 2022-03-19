from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Curso
from Prueba.forms import CreateUser, CursoFormulario, BusquedaCurso
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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.info(request,"Usuario o Contraseña incorrecta")
    
    context = {}
    return render(request, 'diseño/accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        f = CreateUser(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Cuenta creada correctamente')
            return redirect('login')

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

def cursos_create(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada']) 
            curso.save()
            return render(request, "diseño/cursos.html", {"curso":curso})
    else: 
        miFormulario= CursoFormulario()
    return render(request, "diseño/cursos.html", {"miFormulario":miFormulario})

def buscar(request):

    cursos = []
    dato = request.GET.get('partial_curso', None)

    if dato is not None:
        cursos = Curso.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaCurso()
    return render(request, "diseño/buscador.html", {'buscador': buscador, 'cursos': cursos, 'dato': dato})
