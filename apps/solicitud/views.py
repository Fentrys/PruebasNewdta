from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.solicitud.forms import SolicitudForm, ContactosdForm

# Create your views here.

def index(request):
  return render(request, 'index.html')

def nosotros(request):
  return render(request, 'nosotros.html')

def servicio(request):
  return render(request, 'servicio.html')

def contacto(request):
  if request.method == 'POST':
      form = ContactosdForm(request.POST)
      if form.is_valid():
        form.save();
      return redirect('/')
  else:
      form = ContactosdForm()

  return render(request, 'contacto.html', {'form':form})

def precios(request):
  return render(request, 'precios.html')

def solicitud(request):
  if request.method == 'POST':
      form = SolicitudForm(request.POST)
      if form.is_valid():
        form.save();
      return redirect('/')
  else:
      form = SolicitudForm()

  return render(request, 'solicitud.html', {'form':form})

def ticket(request):
  return render(request, 'ticket.html')