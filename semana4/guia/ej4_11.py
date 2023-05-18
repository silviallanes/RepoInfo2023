'''11-Crea una función llamada contar_vocales que tome una cadena de texto como
parámetro y devuelva el número de vocales que contiene.'''

def contar_vocales(texto):
       
    vocales = "aeiouAEIOUáéíóú"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    print("El número de vocales en el texto es:", contador)

cadena = "Silvia Susana Llanes"
contar_vocales(cadena)