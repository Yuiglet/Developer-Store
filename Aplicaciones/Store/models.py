from django.db import models
from .choices import tiposP
# Create your models here.
class Usuario(models.Model): 
    Correo = models.CharField(max_length=50)
    NomUsuario = models.CharField(max_length=30) 
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=40)
    NPregunta = models.CharField(max_length=10)
    Respuesta = models.CharField(max_length=50)
    Contrasena = models.CharField(max_length=100)
    class Meta:
     verbose_name = 'Usuario'
     verbose_name_plural = 'Usuarios'
     db_table = 'usuario'
class Proyecto(models.Model):
    NomProyecto = models.CharField(max_length=40)
    DesProyecto = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    TipoProyecto = models.CharField(max_length=10, choices= tiposP, default='Escritorio')
    imgsProyecto = models.ImageField(verbose_name='ImagenDelProyecto')
    LinkProyecto = models.CharField(max_length=400)


