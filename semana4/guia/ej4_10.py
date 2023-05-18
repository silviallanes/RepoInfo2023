'''10-Crea una función llamada calcular_factorial que tome un número entero como
parámetro y devuelva el factorial de ese número. El factorial de un número
entero positivo n se define como el producto de todos los números enteros
positivos desde 1 hasta n.'''

def factorial(numero):
    fact = 1
    for i in range(1, numero + 1):
        fact *=  i
    print("El factorial de", numero, "es", fact)
    
num = input("ingrese el valor para calcular el factorial: ")
factorial(int(num))