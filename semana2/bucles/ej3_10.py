#10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
#la misma cadena pero con todas las vocales en mayúscula.
cadena = input("ingrese una secuencia de caracteres: ")
lista_cadena = list(cadena)
i = 0
while i <  len(lista_cadena):
    if lista_cadena[i] == "a" or lista_cadena[i] == "e" or lista_cadena[i] == "i" or lista_cadena[i] == "o" or lista_cadena[i] == "u":
        lista_cadena[i] = lista_cadena[i].upper()
    i += 1
cadena_generada = "".join(lista_cadena)

print("la cadena resultante es: ",cadena_generada)
