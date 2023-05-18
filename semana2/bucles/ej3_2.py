#2-Escribe un programa que pida al usuario un número y calcule la suma de todos
#los números naturales del 1 hasta ese número.
numero = int(input("ingrese un numero mayor a cero: "))
suma = 0
i = 0
while i <= numero:
    suma += i
    i += 1
print("la suma total es: ", suma) 