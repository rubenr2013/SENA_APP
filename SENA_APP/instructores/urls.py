from django.urls import path
from . import views
from .views import InstructorFormView

app_name = 'instructores'
urlpatterns = [
    path('instructores/', views.instructores, name='lista_instructores'),
    path('instructores/instructor/<int:instructor_id>/', views.detalle_instructor, name='detalle_instructor'),
    path('crear_instructor/', InstructorFormView.as_view(), name='crear_instructor'),
]
