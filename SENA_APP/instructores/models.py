from django.db import models

# Create your models here.


class Instructor(models.Model):
    NIVEL_EDUCATIVO_CHOICES = [
        ('TEC', 'Tecnico'),
        ('TGL', 'Tegnologo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especializacion'),
        ('MAE', 'Maestria'),
        ('DOC', 'Doctorado'),
    ]
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cedula de Ciudadania'),
        ('CE', 'Cedula de Extranjeria'),
        ('TI', 'Tarjeta de Identidad'),
        ('PA', 'Pasaporte'),
    ]
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default='CC')
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=100, null=True)
    nivel_educativo = models.CharField(max_length=3, choices=NIVEL_EDUCATIVO_CHOICES, default='MAE')
    especialidad = models.CharField(max_length=100)
    anios_experiencia = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField(auto_now_add=True)
    

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    def __str__(self):
        return f"{self.nombre_completo()} - {self.documento_identidad}"