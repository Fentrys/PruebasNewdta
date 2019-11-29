from django.db import models

# Create your models here.
class Ticket(models.Model):
  IdTicket=models.IntegerField(primary_key = True)
  Usuario= models.CharField(max_length=100)
  FechaAbierto=models.DateField()
  Correo= models.CharField(max_length=150)
  Telefono= models.CharField(max_length=50)
  Problema= models.CharField(max_length=90)
  ExplicacionProblema=models.TextField()
  