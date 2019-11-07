class Nodo:#se creara la clase llamada nodo
    def __init__(self,dato):#se le insertó el método constructor
        self.siguiente = None# se creo la variable siguiente
        self.info=dato#la clase info se tomara para que sea igual a dato
    def verNodo(self):# se crea un método para que retorne el dato
        return self.info#

    
   

class Lista:#se creó otra clase para listar
    def __init__(self):#se creó el método constructor
        self.primero = None #el primer dato sera nulo

    def vacia(self):#este método define si la lista esta vacia  
        if self.primero == None: #si la  variable primero es igual a vacia se retornará verdadero u falso
            return True
        else:
            return False

 def insertarPrimero(self,introducir_dato): #se creó el método  para insertar el primer dato
        temporal = Nodo(introducir_dato) #se creó  una variable llamada temporal la cual la cual será igual a la clase nodo y introducir datos
        temporal.siguiente = self.primero
        self.primero = temporal

  def listar(self):
     print('*****lista de polinomios******')
       temporal=self.primero
       while temporal != None:
           print(temporal.verNodo(),end=',')
           temporal = temporal.siguiente
