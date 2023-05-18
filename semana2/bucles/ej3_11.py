'''11-Escribe un programa que pida al usuario un número y calcule su factorial.
Un factorial es el producto que resulta de multiplicar un número entero positivo
dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
de 4 es 4! = 4 × 3 × 2 × 1 = 24.'''
numero = int(input("ingrese un numero para calcular el factorial: "))
fact = 1
cont = 1
if numero == 0 or numero == 1:
    fact = 1
else:
    while cont <= numero:
        fact *= cont
        cont += 1
print(" el factorial de ", numero, " es: ", fact)
