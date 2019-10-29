class Nodo:
    def __init__(self,dato):
        self.siguiente = None
        self.info=dato
    def verNodo(self):
        return self.info
class Lista:
    def __init__(self):
        self.primero = None

    #def vacia(self):
     #   if self.primero == None:
      #      return True
       # else:
        #    return False

