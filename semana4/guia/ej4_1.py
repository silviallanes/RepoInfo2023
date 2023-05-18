'''1-Crea una función llamada suma que tome dos números como parámetros y
devuelva la suma de ellos.'''
#parametro por posicion

def suma(num1, num2):
    total = num1 + num2
    return total

# distintas formas de llamar e imprimir el valor
print("El total es ", suma(8, 2))

total_sum = suma(9, 5)
print(f"el total es {total_sum}")