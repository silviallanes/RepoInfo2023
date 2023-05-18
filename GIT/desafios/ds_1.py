#Se te pide crear un programa que le pida al usuario que ingresar un texto
#cualquiera, por ejemplo, un artículo o una frase.
#Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
#elección.
cadena = input("Ingrese un texto: ").lower()
letra1 = input("ingrese la primera letra: ").lower()
letra2 = input("ingrese la segunda letra: ").lower()
letra3 = input("ingrese la tercera letra: ").lower()
#1- encontrar la cantidad de veces que esta cada letra en la cadena de caracteres ingresada
lista_texto = list(cadena)
print("Cantidad de veces que aparece ", letra1, " en el texto: ", lista_texto.count(letra1))
print("Cantidad de veces que aparece ", letra2, " en el texto: ", lista_texto.count(letra2))
print("Cantidad de veces que aparece ", letra3, " en el texto: ", lista_texto.count(letra3))