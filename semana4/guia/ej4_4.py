'''4-Crea una función llamada es_capicua que tome un número como parámetro y
devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
derecha a izquierda) y False en caso contrario.'''
def capicua(numero):
    return (numero == numero[::-1])
nro = input("Ingrese un número para determinar si es capicúa: ")
if (capicua(nro)):
    print("el numero ingresado es capicua")
else: 
    print("el nro ingresado no es capicua")
    