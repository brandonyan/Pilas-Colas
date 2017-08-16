class Pelicula():
    def  __init__ (self,  genero, anio, actor):
        self.Genero=genero
        self.Anio=anio
        self.Actor=actor

from Pila import *
def inicio():
    
    pila1=Pila()
    pila2=Pila()
    
    print("Bienvenido")
    while True:
        print ("1-Agregar Pelicula")
        print ("2-buscar Pelicula")
        print ("3-cantidad de Peliculas")
        print ("4-Salir")
        x=input("digite una opcion: ")
        x=int(x)
        if x==1:
            
            genero=input("genero de la Pelicula? ")
            anio=input("anio de la Pelicula? ")
            actor=input("actor de la Pelicula? ")
            pelicula=Pelicula(genero,anio,actor)            

            pila1.apilar(pelicula)
        elif x==2:
            p=input("anio de la Pelicula? ")
            while len(pila1.items) != 0:
                pelicula=pila1.desapilar()
                pila2.apilar(pelicula)
                if(p==pelicula.Anio):
                    print (pelicula.Actor)

            while len(pila2.items)!= 0:
                pelicula=pila2.desapilar()
                pila1.apilar(pelicula)            
                
        elif x==3:
            print (len(pila1.items))
        elif x==4:
            break
        else:
            print ("ingrese una opcion valida")
