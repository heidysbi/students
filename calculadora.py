def suma(numero1, numero2):
    return numero1 + numero2

def resta (num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2): 
    if num2 == 0:
        return "No puedes dividir entre cero!"
    else:
        return num1 / num2


def rango(inicio, fin):
    for i in range (fin):
        yield i ** 2

#def sumatoria(num1, num2)
 #   return num1 + num2

def sumatoria(*args):
    return sum(args)

def random(nombre, **kwargs):
    size = random.randint(6, 15)
    lista = []
    for i in range(size):
        number = random.randint(97, 122)
        letter = chr(number)
        #Ascci
        lista.append

   
