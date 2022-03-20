from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Curso, Order, Producto, Usuario
from Prueba.forms import CreateUser, CursoFormulario, BusquedaCurso, OrderForm
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


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
    f = CreateUser(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            user = f.save()
            username = f.cleaned_data.get('username')

            group = Group.objects.get(name='usuario')
            user.groups.add(group)

            Usuario.objects.create(
				user=user,
				nombre=user.username,
				)

            messages.success(request, 'Cuenta creada: ' + username)
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
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'], precio=informacion['precio'],
            descripcion=informacion['descripcion']) 
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


def productos(request):
    productos = Curso.objects.all()
    
    return render(request, 'diseño/accounts/productos.html', {'productos': productos})

def view_usuarios(request):
    usuarios = Usuario.objects.all()

    return render(request, 'diseño/accounts/usuario.html', {'usuarios':usuarios})

def usuario(request, pk_test):
    usuario = Usuario.objects.get(id=pk_test)
    
    orders = usuario.order_set.all()
    order_count = orders.count()

    context = {'usuario': usuario, 'orders': orders, 'order_count': order_count}
    return render(request, 'diseño/accounts/cliente.html', context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'diseño/accounts/order.html', context)

def updateOrder(request, pk):

	order = Curso.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = CursoFormulario(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'diseño/accounts/order.html', context)

def deleteOrder(request, pk):
	order = Curso.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('productos')

	context = {'item':order}
	return render(request, 'diseño/accounts/delete.html', context)

def userPage(request):
    orders = request.user.usuario.order_set.all()

    context = {'orders':orders}
    return render(request, 'diseño/accounts/user.html')