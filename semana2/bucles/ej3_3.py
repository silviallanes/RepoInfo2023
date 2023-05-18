#3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
#multiplicar correspondiente a ese número del 1 al 10.
numero = int(input("ingrese el numero: "))
i = 0
for i in range(11):
    print(numero, " * ",i," = ", numero* i,end="\n")