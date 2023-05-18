##17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
##en orden inverso.
##Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
##"mundo hola".
##Importante!!! Utiliza un solo print()
a = input("ingrese una frase ")
a_split = a.split()
print(a_split[1]+ " "+ a_split[0])
