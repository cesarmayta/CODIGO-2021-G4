"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from cursos.views import consultarCursos
from cursos.views import consultarAlumnos
from cursos.views import registrarCurso



def principal(request):
    return HttpResponse("<center><h1>PAGINA PRINCIPAL</h1></center>")

urlpatterns = [
    path('',principal),
    path('cursos/',consultarCursos,name='cursos'),
    path('alumnos/',consultarAlumnos,name='alumnos'),
    path('registrarCurso/',registrarCurso,name='registrarCurso'),
    path('admin/', admin.site.urls),
]
