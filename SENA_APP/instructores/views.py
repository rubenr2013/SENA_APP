from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.contrib import messages
from .models import Instructor
from .forms import InstructorForm

# Lista de instructores
def instructores(request):
    lista_instructores = Instructor.objects.all().order_by('apellido', 'nombre')
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructores,
        'total_instructores': lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))

# Detalle de un instructor
def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    cursos_coordinados = instructor.cursos_coordinados.all()
    cursos_impartidos = instructor.cursos_impartidos.all()
    template = loader.get_template('detalle_instructor.html')
    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    return HttpResponse(template.render(context, request))

# Formulario para crear instructor
class InstructorFormView(FormView):
    template_name = 'crear_instructor.html'
    form_class = InstructorForm
    success_url = reverse_lazy('instructores:lista_instructores')

    def form_valid(self, form):
        instructor = form.save()
        messages.success(
            self.request,
            f'El instructor {instructor.nombre} {instructor.apellido} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)
