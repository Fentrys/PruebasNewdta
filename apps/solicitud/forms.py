from django import forms

from apps.solicitud.models import Solicitudes, Contactos


class SolicitudForm(forms.ModelForm):
    
    class Meta:
        model = Solicitudes
        
        fields = ['Nombre',
        'Apellido',
        'Paquete',
        'Correo',
        'Telefono',
        'Fecha',
        'Comentarios',
        ]

        labels ={'Nombre':'Nombre',
        'Apellido':'Apellido',
        'Paquete':'Paquete',
        'Correo':'Correo',
        'Telefono':'Telefono',
        'Comentarios':'Comentarios',
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Apellido': forms.TextInput(attrs={'class':'form-control'}),
            'Paquete': forms.TextInput(attrs={'class':'form-control'}),
            'Correo': forms.TextInput(attrs={'class':'form-control'}),
            'Telefono': forms.TextInput(attrs={'class':'form-control'}),
            'Fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'Comentarios': forms.Textarea(attrs={'class':'form-control'}),
        }

class ContactosdForm(forms.ModelForm):
    
    class Meta:
        model = Contactos
        fields = ['Nombre_completo',
        'Telefono',
        'Correo',
        'Comentario',        
        ]

        labels ={'Nombre_completo':'Nombre completo',
        'Telefono':'Telefono',
        'Correo':'Correo',
        'Comentario':'Comentario',
        }

        widgets = {
            'Nombre_completo': forms.TextInput(attrs={'class':'form-control'}),
            'Telefono': forms.TextInput(attrs={'class':'form-control'}),
            'Correo': forms.TextInput(attrs={'class':'form-control'}),            
            'Comentario':  forms.Textarea(attrs={'class':'form-control'}),
        }