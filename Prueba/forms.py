from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form
from ckeditor.fields import RichTextFormField
from Prueba.models import Curso, Ordene, Usuario  
  
class CreateUser(UserCreationForm):  
    
    username = forms.CharField(label='Usuario', min_length=5, max_length=150)  
    email = forms.EmailField(label='Email')  
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El usuario ya existe")
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("El Email ya existe")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("La contraseña no coincide") 
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  


class CursoFormulario(forms.Form):
    
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    precio = forms.FloatField()
    descripcion = forms.CharField(max_length=200)
    presentacion = RichTextFormField(required=False)
    imagen = forms.ImageField()
    

class ProfesorFormulario(forms.Form):   

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class BusquedaCurso(forms.Form):

    partial_curso = forms.CharField(label='Buscar', max_length=100)


class OrderForm(forms.ModelForm):

	class Meta:
		model = Curso
		fields = '__all__'


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['user', 'nombre']
        profile_pic = forms.ImageField()


class OrdenesForm(forms.ModelForm):

	class Meta:
		model = Ordene
		fields = '__all__'

class ContactForm(forms.Form):
	nombre= forms.CharField(max_length = 50)
	email = forms.EmailField(max_length = 150)
	mensaje = forms.CharField(widget = forms.Textarea, max_length = 2000)