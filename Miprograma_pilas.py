class pila:#se crea una clase
    def __init__(self,cantidad = int(10)):#se creo el método constructor
        self.datos = []# en esta variable se agregarán los datos una vez hechas las operaciones
        self.top = -1#el dato no puede ser nagativo
        self.cantidad = cantidad##contidad de números que se pueden introducir
        
    
    def adiciona_sacar(self,dato):#se crea el método para adiccionar y sacar de la lista que vamos a crear
        if self.top < self.cantidad :# esta instrucción tiene como regla que si el tope es menor a la cantidad
            self.top += 1 #se le podrá agregar elementos
            self.datos.append(dato)  #despues adiciono
            
            if dato < 0:#si el dato es menor a cero se quitará
               self.datos.pop()

            elif (dato %2 != 0):#si no se realizó la anterior operación
                self.datos.pop()#se realizará esta operación que quitara el dato no es número par

            elif dato == 0:#si no se realizó la anterior operación
                self.datos.clear() #si dato es cero se eliminará


