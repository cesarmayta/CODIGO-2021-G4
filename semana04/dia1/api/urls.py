from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('alumnos',views.alumnos),
    path('profesores',views.profesores),
    path('profesores/<int:profesor_id>',views.profesor)
]