#8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
#el número de palabras que contiene.
cadena = input("ingrese un texto: ")
lista_cadena = cadena.split()
print("total de palabras ", len(lista_cadena))
