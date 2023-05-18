texto = input("agregue texto: ")

palabras = texto.split()
print("palabras ", palabras)

palabras_invertidas = palabras[::-1]
print("palabras invertidas", palabras_invertidas)

texto_invertido = " ".join(palabras_invertidas)

print(texto_invertido)