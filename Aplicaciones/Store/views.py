from django.shortcuts import render
from .models import Usuario
from django.shortcuts import redirect, render
import html

# Create your views here.
def home (request):
    data = {
        'titulo': 'Registro'
    }
    return render (request, "reg.html",data)
def new_user(request):
 CorreoP = request.POST['txtCorreo']
 Correo = html.escape(CorreoP)
 NomUsuario = request.POST['txtUsuario']
 Nombre = request.POST['txtNombre']
 Apellido = request.POST['txtApellido']
 NPregunta = request.POST['txtNPregunta']
 Respuesta = request.POST['txtRespuesta']
 Contrasena = request.POST['txtContrasena']
 usuario = Usuario.objects.create(Correo = Correo,NomUsuario = NomUsuario, Nombre = Nombre, Apellido = Apellido, NPregunta = NPregunta, Respuesta = Respuesta, Contrasena = Contrasena )
 return redirect('/MyUser/')
def my_user(request):
   return render (request, "MiPerfil.html")
def login(request):
   return render (request,"Login.html" )
def Log_in(request):
    CorreoP = request.POST['txtCorreo']
    Correo = html.escape(CorreoP)
    Contrasena = request.POST['txtContrasena']
    usuario = Usuario.objects.filter(Correo = Correo, Contrasena = Contrasena).exists()
    if usuario:
        usuarioD = Usuario.objects.get(Correo = Correo)
        datosObt = []
        usuarioD.NomUsuario = datosObt
        return redirect ('/MyUser/', usuarioD, request)


    
   