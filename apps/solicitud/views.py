from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return render(request, 'index.html')

def nosotros(request):
  return render(request, 'nosotros.html')

def servicio(request):
  return render(request, 'servicio.html')

def contacto(request):
  return render(request, 'contacto.html')

def precios(request):
  return render(request, 'precios.html')

def solicitud(request):
  return render(request, 'solicitud.html')

def ticket(request):
  return render(request, 'ticket.html')