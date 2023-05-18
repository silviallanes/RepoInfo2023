#13-Escribe un programa que pida al usuario un número y luego imprima un
#triángulo de asteriscos con esa cantidad de filas.
nro = int(input("ingrese un numero: "))
i = 1
while i <= nro:
    j = 1
    while j <= i:
        print("*",end="")
        j += 1
    i += 1
    print("\n")

    
