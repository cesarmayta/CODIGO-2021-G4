class clsAlumno:
    
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print(self.nombre + " - " + self.email)
        
    def getNombre(self):
        return self.nombre

        
opcion = ''
listaObjectosAlumnos = []



print("====================================")
print("    REGISTRO DE ALUMNOS             ")
print("====================================")

while(opcion != 'salir'):
    opcion = input("OPCIONES (registrar,mostrar,salir) : ")
    if(opcion != 'salir'):
        if(opcion == "registrar"):
            nombre = input("NOMBRE DEL ALUMNO : ")
            email = input("EMAIL DEL ALUMNO : ")
            objNuevoAlumno = clsAlumno(nombre,email)
            listaObjectosAlumnos.append(objNuevoAlumno)
        elif(opcion == "mostrar"):
            for objAlumno in listaObjectosAlumnos:
                objAlumno.mostrar()
        else:
            print("LA OPCIÓN NO ES VALIDA")
            