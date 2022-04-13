from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Curso, Ordene, Producto, Usuario
from Prueba.forms import CreateUser, CursoFormulario, BusquedaCurso, OrdenesForm, OrderForm, ProfileForm, ContactForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.core.mail import send_mail, BadHeaderError


def inicio(request):

    return render(request, "diseño/index.html", {})


@permission_required('usuario', login_url="login")
def cursos(request):

    return render(request, "diseño/cursos.html", {})


def sobremi(request):

    return render(request, "diseño/sobremi.html", {})


@login_required(login_url="login")
def contacto(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            asunto = "Adquirir" 
            informacion = {
            'nombre': form.cleaned_data['nombre'], 
            'email': form.cleaned_data['email'], 
            'mensaje':form.cleaned_data['mensaje'], 
            }
            mensaje = "\n".join(informacion.values())

            try:
                send_mail(asunto, mensaje, 'rodrigo.javi@hotmail.com', ['rodrigo.javi@hotmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("Contacto")
        
    form = ContactForm()
    return render(request, "diseño/contacto.html", {'form':form})
    

def entrada(request):
    
    return render(request, "diseño/entrada.html", {})


@user_passes_test(lambda u: u.is_anonymous, login_url="inicio")
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.info(request,"Usuario o Contraseña incorrecta")
    
    context = {}
    return render(request, 'diseño/accounts/login.html', context)


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get_or_create(name='Usuario')
            user.groups.add(group)
            Usuario.objects.create(
                user=user,
                nombre=user.username,
                email=email,
                )

            messages.success(request, 'Cuenta creada ' + username)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'diseño/accounts/register.html', context)


@login_required(login_url="login")
def cursos(request):

    return render(request, "diseño/cursos.html", {})


@login_required(login_url="login")
def curso(request):
    
    productos = Curso.objects.all()
    form = ProfileForm()
    cursos = []
    dato = request.GET.get('partial_curso', None)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    if dato is not None:
        cursos = Curso.objects.filter(nombre__icontains=dato)
    
    buscador = BusquedaCurso()
    return render(request, "diseño/buscador.html", {'buscador': buscador, 'cursos': cursos, 'dato': dato, 'productos': productos, 'form': form})





@user_passes_test(lambda u: u.is_superuser, login_url="inicio")
def view_usuarios(request):

    usuarios = Usuario.objects.all()

    return render(request, 'diseño/accounts/usuario.html', {'usuarios':usuarios})


def usuario(request, pk_test):

    usuario = Usuario.objects.get(id=pk_test)
    
    orders = usuario.ordene_set.all()
    order_count = orders.count()

    context = {'usuario': usuario, 'orders': orders, 'order_count': order_count}
    return render(request, 'diseño/accounts/cliente.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url="inicio")
def crear_curso(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'], precio=informacion['precio'],
            descripcion=informacion['descripcion'], presentacion=informacion['presentacion'], imagen=informacion['imagen']) 
            curso.save()
            return render(request, "diseño/accounts/productos.html", {"curso":curso, "miFormulario": miFormulario})
    else: 
        miFormulario= CursoFormulario()
    productos = Curso.objects.all()

    return render(request, 'diseño/accounts/productos.html', {'productos': productos, 'miFormulario': miFormulario})


@user_passes_test(lambda u: u.is_superuser, login_url="inicio")
def modificar_curso(request, pk):

	order = Curso.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST,request.FILES, instance=order)
		if form.is_valid():
			form.save()
			return redirect('Cursos')

	context = {'form':form}
	return render(request, 'diseño/accounts/order.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url="inicio")
def borrar_curso(request, pk):

	order = Curso.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('productos')

	context = {'item':order}
	return render(request, 'diseño/accounts/delete.html', context)


@login_required(login_url="login")
def user_page(request):
    
    orders = request.user.usuario.ordene_set.all()

    total_orders = orders.count()

    context = {'orders':orders, 'total_orders':total_orders}
    return render(request, 'diseño/accounts/user.html', context)


@login_required
def configuracion(request):
    
    user = request.user.usuario
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'diseño/accounts/user_config.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url="inicio")
def crear_compra(request):

	form = OrdenesForm()
	if request.method == 'POST':

		form = OrdenesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'diseño/accounts/order.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url="inicio")
def modificar_compra(request, pk):

	order = Ordene.objects.get(id=pk)
	form = OrdenesForm(instance=order)

	if request.method == 'POST':
		form = OrdenesForm(request.POST,request.FILES, instance=order)
		if form.is_valid():
			form.save()
			return redirect('Cursos')

	context = {'form':form}
	return render(request, 'diseño/accounts/order.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url="inicio")
def borrar_compra(request, pk):

	order = Ordene.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('usuarios')

	context = {'item':order}
	return render(request, 'diseño/accounts/delete2.html', context)