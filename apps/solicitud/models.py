from django.db import models

# Create your models here.
class Solicitudes(models.Model):
  IdSolicitud = models.AutoField(primary_key=True)
  Nombre = models.CharField(max_length=60)
  Apellido = models.CharField(max_length=60)
  Paquete = models.CharField(max_length=90)
  Correo = models.CharField(max_length=100)
  Telefono = models.CharField(max_length=40)
  Fecha = models.DateField()
  Comentarios = models.TextField()


class Contactos(models.Model):
  IdContactos= models.AutoField(primary_key=True)
  Nombre_completo= models.CharField(max_length=150)
  Telefono= models.CharField(max_length=50)
  Correo= models.CharField(max_length=150)
  Comentario= models.TextField()