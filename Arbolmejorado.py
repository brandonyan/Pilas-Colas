class Nodo():
    def __init__(self, valor, izq=None, der=None):
        self.valor=valor
        self.izq=izq
        self.der=der
        
class Variable():
    def  __init__ (self, nombre, valor):
        self.Nombre=nombre
        self.Valor=valor

def evaluar(arbol):     
    if arbol.valor == "+":
        return (arbol.izq) + (arbol.der)
    elif arbol.valor == "-":
        return (arbol.izq) - (arbol.der)
    elif arbol.valor == "*":
        return (arbol.izq) * (arbol.der)
    elif arbol.valor == "/":
        return (arbol.izq) / (arbol.der)
    
    return int(arbol.valor)


    
from Pila import *
def inicio():
    
    pila=Pila()
    pila2=Pila()
    pila3=Pila()

    print("ingrese vacio para Terminar")
    while True:
        m=raw_input("ingreso en post-orden:").split(" ")
        k=len(m)
            if m == '':
                break
                print("final")

            if k == 0:
                break
                print("final")
            
            for j in range(0, k):
                y=m[j]

            

            if(y=="="):
                while len(pila2.items) != 0:
                    variable=pila2.desapilar()
                    pila3.apilar(variable)
                    print(variable.Nombre,"=",variable.Valor)

                                
            elif y in ["+", "-", "*", "/"]:
                if(len(pila.items)>=2):
                    der=pila.desapilar()
                    izq=pila.desapilar()
                    nodo=Nodo(y, izq, der)

                    x=evaluar(nodo)
                    pila.apilar(x)
                else:
                    print("estructura incorrecta")
            else:
                try:
                    y=int(y)
                    pila.apilar(y)
                except:
                    if(m[j+1]=="="):
                        variable=Variable(y,pila.desapilar())
                        pila2.apilar(variable)
                        
                        print("variable correcta")
                    else:
                        while len(pila2.items) != 0:
                            variable=pila2.desapilar()
                            pila3.apilar(variable)
                            if(y==variable.Nombre):
                                pila.apilar(variable.Valor)

                        while len(pila3.items)!= 0:
                            variable=pila3.desapilar()
                            pila2.apilar(variable)
            
            

    print(pila.desapilar())
            

                
                
                
            
