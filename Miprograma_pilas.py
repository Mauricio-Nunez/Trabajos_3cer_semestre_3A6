class pila:#se crea una clase
    def __init__(self,cantidad = int(10)):#se creo el método constructor
        self.datos = []# en esta variable se agregarán los datos una vez hechas las operaciones
        self.top = -1#el dato no puede ser nagativo
        self.cantidad = cantidad##contidad de números que se pueden introducir

    