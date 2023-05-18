#14-Escribe un programa que pida al usuario un número y luego imprima un
#triángulo de números como el siguiente:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
nro = int(input("ingrese un numero: "))
i = 1
while i <= nro:
    j = 1
    while j <= i:
        print(i,end="")
        j += 1
    i += 1
    print()
