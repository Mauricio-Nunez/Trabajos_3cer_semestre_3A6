
def Conversor_Octal(n):    #definimos un método
   if n <= 8 or n==8 :              #si no se cumple la condición
       return n            #regresará el valor del número que se aiga introducido
   else:                   #pero si no se cumple esta condición
        return Conversor_Octal(int( n / 8 )),Conversor_Octal( n % 8 )#recursivamente se traera el método y lo dividiremos entre 8 ya que esta es a la base que queremos transformar al igual que se obtendra el residuo
#_____
print("_____________Octal_______________")
Conversor_Octal = Conversor_Octal(20)             #al método se le agregará un número al cual se le convertira a base octal
print(Conversor_Octal)


def ConversorHex(n):           #crearemos otro método
    if (n < 0):             #agregaremos una condicional,si el valor a introoducir es menor a cero
        print(0)            #imprimira el número cero
    elif (n<=1):            #si  no se cumple la condición anterior imprimir número en linea
        print (n, end = '')
    else:                   #si no se llamará recursivamente al método que creamos
        ConversorHex(int( n / 16 ))#el cual convertimos en entero para que no nos salgan puntos decimales y el número a introducir un número lo dividimos entre la base 16
        x =(int(n%16))      #creamos una variable la cual contendra el número de el método le sacaremos su residuo
                if (x < 10):        #crearemos una condicional que mientras la variable x sea menor a 10
            print(x)       #se imprimira x

        if (x == 10):       #si no si la variable x es igual a 10
            print("A")     #se cambiará por la letra A y ASI SERÁ CON EL RESTO HASTA LLEGAR A F el cual será 15

        if (x == 11):
            print("B")

        if (x == 12):
            print("C")

        if (x == 13):
            print("D")

        if (x == 14):
            print("E")

        if (x == 15):
            print ("F")
