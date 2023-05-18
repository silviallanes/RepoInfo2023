'''5-Crea una función llamada es_divisible que tome dos números enteros como
parámetros y devuelva Es divisible si el primer número es divisible por el
segundo número, o No es divisible en caso contrario'''
def divisible(x,z):
    return (x % z == 0)

a = int(input("ingrese dividendo: "))
b = int(input("ingrese divisor: "))
if divisible(a,b):
    print(f"{a} es divisible por {b}")
else:
    
    print(f"{a} no es divisible por {b}")