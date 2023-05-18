'''7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número.'''
def imprimir_pares(nro):
    for i in range(1, nro):
        if i % 2 == 0:
            print(i, end=" - ")

a = input("ingrese un numero: ")
if a.isdigit():
    imprimir_pares(int(a))
else:
    print("lo ingresado no es un numero")