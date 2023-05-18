'''18-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 3
4 5 6
7 8 9 10'''
numero = int(input("ingrese un numero: "))
i = 1
j = 1
cont = 1
while cont < numero:
    while i >= j:
        print(cont,end=" ")
        cont += 1
        j += 1
    print()
    i += 1
    j = 1
        
    

