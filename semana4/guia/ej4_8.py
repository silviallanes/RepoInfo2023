'''8-Crea una función llamada es_palindromo que tome una cadena de texto como
parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
contrario.'''

def es_palindromo(cadena):
    if cadena == cadena[::-1]:
        print("La cadena es un palíndromo")
    else:
        print("La cadena no es un palíndromo")

texto = "anita lava la tina"
text2 = texto.replace(" ", "") # eliminamos los espacios en blanco

es_palindromo(text2)