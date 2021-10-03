from tkinter import  *
from tkinter.ttk import Treeview

class Alumno:
    
    def agregar(self):
        self.trvAlumnos.insert('',0,text= self.nombre.get(),values = self.email.get())
    
    def __init__(self,window):
        self.window = window
        self.window.title("Alumnos")
        
        #FRAME
        frame = LabelFrame(self.window,text="Registro de Nuevo Alumno")
        frame.grid(row=0,column=0,columnspan=3,pady=10)
        #ETIQUIETA
        lbNombre = Label(frame,text= 'Nombre : ')
        lbNombre.grid(row=1,column=0)
        #CAJA DE TEXTO
        self.nombre = Entry(frame)
        self.nombre.grid(row=1,column=1)
        
        #CAMPO PARA EMAIL
        lbEmail = Label(frame,text="Email : ")
        lbEmail.grid(row=2,column=0)
        
        #caja de texto para email
        self.email = Entry(frame)
        self.email.grid(row=2,column=1)
        
        #BOTON PARA NUEVO ALUMNO
        btnNuevoAlumno = Button(frame,text="Agregar",command=self.agregar)
        btnNuevoAlumno.grid(row=4,columnspan=2,sticky=W + E)
        
        #CREAMOS TREEVIEW
        self.trvAlumnos = Treeview(height=10,columns=2)
        self.trvAlumnos.grid(row=5,column=0,columnspan=2)
        self.trvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email',anchor=CENTER)
        
window = Tk()
app = Alumno(window)
window.mainloop()