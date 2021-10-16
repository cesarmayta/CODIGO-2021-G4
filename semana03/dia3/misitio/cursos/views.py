from django.shortcuts import render,redirect

# Create your views here.
from .models import Curso

def consultarCursos(request):
    listaCursos = Curso.objects.all()
    
    context = {
        'lstCursos': listaCursos
    }
    
    return render(request,'cursos.html',context)

def consultarAlumnos(request):
    return render(request,'alumnos.html')

def registrarCurso(request):
    nombreCurso = request.POST['curso']
    if(nombreCurso != ""):
        nuevoCurso = Curso()
        nuevoCurso.nombre = nombreCurso
        nuevoCurso.save()
        return redirect('/cursos')
    else:
        return redirect('/cursos')
    