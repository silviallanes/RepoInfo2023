## ingresar un caracter e imprimir si...
caracter= input("Ingrese un caracter: ")
if caracter.isupper():
    print("el caracter es una mayuscula")
elif caracter.islower():
    print("el caracter es una minuscula")
elif caracter.isdigit():
    print("el caracter es un numero")
else:
    print("el caracter es especial")
    