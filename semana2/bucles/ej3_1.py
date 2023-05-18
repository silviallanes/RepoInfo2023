#1-Escribe un programa que pida al usuario una palabra y luego imprima cada
#letra de la palabra en una línea separada.
palabra = input("ingrese una palabra: ")
for letra in palabra:
    print(letra,end="\n")
print("final")
