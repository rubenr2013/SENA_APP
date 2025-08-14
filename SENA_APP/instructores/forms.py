from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'documento_identidad', 'tipo_documento', 'nombre', 'apellido',
            'telefono', 'correo', 'fecha_nacimiento', 'ciudad', 'direccion',
            'nivel_educativo', 'especialidad', 'anos_experiencia', 'activo',
            'fecha_vinculacion'
        ]
        labels = {
            'documento_identidad': "Documento de Identidad",
            'tipo_documento': "Tipo de Documento",
            'nombre': "Nombre",
            'apellido': "Apellido",
            'telefono': "Teléfono",
            'correo': "Correo Electrónico",
            'fecha_nacimiento': "Fecha de Nacimiento",
            'ciudad': "Ciudad",
            'direccion': "Dirección",
            'nivel_educativo': "Nivel Educativo",
            'especialidad': "Especialidad",
            'anos_experiencia': "Años de Experiencia",
            'activo': "Activo",
            'fecha_vinculacion': "Fecha de Vinculación",
        }
        help_texts = {
            'documento_identidad': "Ingrese el número de documento de identidad del instructor.",
            'tipo_documento': "Seleccione el tipo de documento del instructor.",
            'nombre': "Ingrese el nombre del instructor.",
            'apellido': "Ingrese el apellido del instructor.",
            'telefono': "Ingrese el número de teléfono del instructor.",
            'correo': "Ingrese el correo electrónico del instructor.",
            'fecha_nacimiento': "Ingrese la fecha de nacimiento del instructor.",
            'ciudad': "Ingrese la ciudad de residencia del instructor.",
            'direccion': "Ingrese la dirección del instructor.",
            'nivel_educativo': "Seleccione el nivel educativo del instructor.",
            'especialidad': "Ingrese la especialidad del instructor.",
            'anos_experiencia': "Ingrese los años de experiencia del instructor.",
            'activo': "Indique si el instructor está activo.",
            'fecha_vinculacion': "Ingrese la fecha de vinculación del instructor.",
        }
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Opcional'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Opcional'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'Opcional'}),
        }

    def clean_documento_identidad(self):
        documento = self.cleaned_data['documento_identidad']
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento_identidad')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        if not documento or not nombre or not apellido:
            raise forms.ValidationError("Documento, nombre y apellido son obligatorios.")
        return cleaned_data
