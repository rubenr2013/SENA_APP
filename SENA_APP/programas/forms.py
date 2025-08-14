from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'codigo', 'nombre', 'nivel_formacion', 'modalidad',
            'duracion_meses', 'duracion_horas', 'descripcion',
            'competencias', 'perfil_egreso', 'requisitos_ingreso',
            'centro_formacion', 'regional', 'estado', 'fecha_creacion'
        ]
        labels = {
            'codigo': "Código del Programa",
            'nombre': "Nombre del Programa",
            'nivel_formacion': "Nivel de Formación",
            'modalidad': "Modalidad",
            'duracion_meses': "Duración en Meses",
            'duracion_horas': "Duración en Horas",
            'descripcion': "Descripción del Programa",
            'competencias': "Competencias a Desarrollar",
            'perfil_egreso': "Perfil de Egreso",
            'requisitos_ingreso': "Requisitos de Ingreso",
            'centro_formacion': "Centro de Formación",
            'regional': "Regional",
            'estado': "Estado",
            'fecha_creacion': "Fecha de Creación del Programa",
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'competencias': forms.Textarea(attrs={'rows': 3}),
            'perfil_egreso': forms.Textarea(attrs={'rows': 3}),
            'requisitos_ingreso': forms.Textarea(attrs={'rows': 3}),
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if not codigo.isalnum():
            raise forms.ValidationError("El código solo debe contener letras y números.")
        return codigo
