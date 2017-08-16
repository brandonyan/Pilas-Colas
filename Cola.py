class Cola(object):
    def __init__(self):
        self.items=[]

    def encolar(self,x):
        self.items.append(x)

    def esta_vacia(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            estudiante=self.items.pop(0)
            return estudiante.Nombre
        
        
