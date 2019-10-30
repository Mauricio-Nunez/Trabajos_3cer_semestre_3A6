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

 def insertarPrimero(self,introducir_dato):
        temporal = Nodo(introducir_dato)
        temporal.siguiente = self.primero
        self.primero = temporal

  def listar(self):
     print('*****lista de polinomios******')
       temporal=self.primero
       while temporal != None:
           print(temporal.verNodo(),end=',')
           temporal = temporal.siguiente
