#7-Escribe un programa que pida al usuario una palabra y determine si es un
#palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
#izquierda).
palabra = input("ingrese una palabra: ")
palabra2 = palabra[::-1]
if palabra == palabra2:
    print(palabra, " es un palíndromo")
else:
    print(palabra, " no es un palíndromo")