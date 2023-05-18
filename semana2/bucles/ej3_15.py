#15-Escribe un programa que pida al usuario una cadena de texto y determine
#cuántas veces aparece cada letra en la cadena.

texto = input("ingrese una cadena de caracteres: ")
import pandas as pd
phrase = texto
print(pd.Series(list(phrase)).value_counts())