#4-Escribe un programa que imprima los números pares del 1 al 100.
''' determina si un numero es par o impar
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")'''
    
i = 1
for i in range(101):
    if i % 2 == 0:
        print(i,end=" ")
