from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Alumno,Profesor
from .serializers import AlumnoSerializer,ProfesorSerializer

# Create your views here.
def index(request):
    #return HttpResponse("<center><h1>bienvenido a mi api</h1><center>")
    return JsonResponse({'mensaje':'Bienvenido a mi Api'})

@api_view(['GET'])
def alumnos(request):
    lstAlumnos = Alumno.objects.all()
    serAlumnos = AlumnoSerializer(lstAlumnos,many=True)
    return Response(serAlumnos.data)

@api_view(['GET','POST'])
def profesores(request):
    if request.method == 'GET':
        lstProfesores = Profesor.objects.all()
        serProfesores = ProfesorSerializer(lstProfesores,many=True)
        return Response(serProfesores.data)
    elif request.method == 'POST':
        print(request.data)
        serProfesores = ProfesorSerializer(data=request.data)
        if serProfesores.is_valid():
            serProfesores.save()
            return Response(serProfesores.data)
        else:
            return Response(serProfesores.errors)
    
@api_view(['GET','PUT','DELETE'])
def profesor(request,profesor_id):
    objProfesor = Profesor.objects.get(id=profesor_id)
    
    if request.method== 'GET':
        serProfesor = ProfesorSerializer(objProfesor)
        return Response(serProfesor.data)
    elif request.method == 'PUT':
        serProfesor = ProfesorSerializer(objProfesor,data=request.data)
        if serProfesor.is_valid():
            serProfesor.save()
            return Response(serProfesor.data)
        else:
            return Response(serProfesor.errors)
    elif request.method == 'DELETE':
        objProfesor.delete()
        return Response(status=204)
        