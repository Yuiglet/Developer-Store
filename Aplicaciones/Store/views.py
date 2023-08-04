from django.shortcuts import render
from .models import Usuario
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
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
 
def login(request):
   return render (request,"Login.html" )

def Log_in(request):
    CorreoP = request.POST['txtCorreo']
    Correo = html.escape(CorreoP)
    Contrasena = request.POST['txtContrasena']
    usuario = Usuario.objects.filter(Correo = Correo, Contrasena = Contrasena).exists()
    if usuario:
        return HttpResponseRedirect('/Profile/?correo={}'.format(Correo))
    else:
       return redirect('/Login/')

def Profile (request):
    Correo = request.GET.get('correo')
    usuarioD = Usuario.objects.get(Correo = Correo)
    message = request.GET.get('message')
    data = {
        'datos': usuarioD,
        'message': message,
    }
    return render(request, "MiPerfil.html", data)

def edit_proflie(request):
    idU = int (request.POST['id'])
    CorreoP = request.POST['txtCorreo']
    Correo = html.escape(CorreoP)
    NomUsuario = request.POST['txtUsuario']
    Nombre = request.POST['txtNombre']
    Apellido = request.POST['txtApellido']
    Contrasena = request.POST['txtContrasena']

    usuario = Usuario.objects.get(id=idU)
    usuario.Correo = Correo
    usuario.NomUsuario = NomUsuario
    usuario.Nombre = Nombre
    usuario.Apellido = Apellido
    usuario.Contrasena = Contrasena
    usuario.save()
    message = "Perfil modificado correctamente."
    return HttpResponseRedirect(f'/Profile/?correo={Correo}&message={message}')
