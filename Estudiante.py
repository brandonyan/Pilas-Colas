class Estudiante():
    def  __init__ (self,  nombre, codigo, placa):
        self.Nombre=nombre
        self.Codigo=codigo
        self.Placa=placa

from Cola import *
def inicio():
    
    cola=Cola()
    
    print("Bienvenido")
    while True:
        print ("1-Agregar Estudiante")
        print ("2-Lamar Estudiante")
        print ("3-cantidad de Estudiantes")
        print ("4-Salir")
        x=input("digite una opcion: ")
        x=int(x)
        if x==1:
            
            nombre=input("nombre del Estudiante?")
            codigo=input("codigo del Estudiante?")
            placa=input("placa del Estudiante?")
            estudiante=Estudiante(nombre,codigo,placa)
            

            cola.encolar(estudiante)
        elif x==2:
            print (cola.desencolar())
        elif x==3:
            print (len(cola.items))
        elif x==4:
            break
        else:
            print ("ingrese una opcion valida")
            
            
    
