#12-Escribe un programa que pida al usuario una lista de números separados por
#comas y calcule su promedio.
numeros = input("ingrese numeros separados por comas ")
lista_nros = numeros.split(",")
suma = 0
cont = 0
while cont < len(lista_nros):
    suma+= int(lista_nros[cont])
    cont+= 1
print("el promedio es ", suma/len(lista_nros))
