import datetime
#VARIABLES
alumnos = []

def ConvertirFechaEnDias(strFecha):
    resultado = (datetime.datetime.now() - datetime.datetime.fromisoformat(strFecha)).days
    return resultado 
#ENTRADAS
cantidadAlumnos = int(input("¿cuantos alumnos desean registrar? "))
for c in range(cantidadAlumnos):
    nombre = input("INGRESE NOMBRE : ")
    fechanac = input("INGRESE FECHA(AÑO-MES-DIA): ")
    alumno = [
        ConvertirFechaEnDias(fechanac) ,
        {
        'nombre': nombre,
        'fechanac': fechanac
        }
    ]
    alumnos.append(alumno)
    
#PROCESO
alumnos.sort()

    
#SALIDAS
for a in alumnos:
    print(a)

#print(alumnos)