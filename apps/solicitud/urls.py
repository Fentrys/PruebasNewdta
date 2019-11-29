from django.conf.urls import url, include
from apps.solicitud.views import index, nosotros, servicio, contacto, precios, solicitud, ticket


urlpatterns =[
  url(r'^$', index),
  url(r'^nosotros/$', nosotros, name='nosotros'),
  url(r'^servicio/$', servicio, name='servicio'),
  url(r'^contacto/$', contacto, name='contacto'),
  url(r'^precios/$', precios, name='precios'),
  url(r'^solicitud/$', solicitud, name='solicitud'),
  url(r'^ticket/$', ticket, name='ticket'),
]