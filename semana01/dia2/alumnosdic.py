import datetime
#VARIABLES
alumnos = {}

def ConvertirFechaEnDias(strFecha):
    resultado = (datetime.datetime.now() - datetime.datetime.fromisoformat(strFecha)).days
    return resultado 
#ENTRADAS
cantidadAlumnos = int(input("¿cuantos alumnos desean registrar? "))
for c in range(cantidadAlumnos):
    nombre = input("INGRESE NOMBRE : ")
    fechanac = input("INGRESE FECHA(AÑO-MES-DIA): ")
    alumno = {
        ConvertirFechaEnDias(fechanac) : {
        'nombre': nombre,
        'fechanac': fechanac
        }
    }
    alumnos.update(alumno)
    
#PROCESO
alumnos_ordenados = sorted(alumnos)

    
#SALIDAS
for a in alumnos_ordenados:
    print(alumnos[a])

#print(alumnos)