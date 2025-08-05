from django.urls import path
from . import views

urlpatterns = [
    path('', views.aprendices, name='lista_aprendices'),
    path('aprendices/', views.aprendices, name='lista_aprendices'),
    path('lista_cursos/', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
]
