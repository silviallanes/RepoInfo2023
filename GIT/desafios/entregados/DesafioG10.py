# INTEGRANTES: 
#JUAN PABLO DIAZ, MARIA ANTONELLA GOMEZ, FERNANDO FERREYRA, 
#LUCAS CARDENA, JORGE LUCAS, RAFAEL LEGUIZAMON
# BRUNO ZALAZAR, VALENTINA PORTILLO, MAURICIO CARDOZO Y SILVIA LLANES

print("\n")

texto = input("Ingrese un texto: ")
letras = input("Ingrese 3 letras separadas por espacios: ").lower().split()

print("\n")

#1- Cantidad de veces que aparece cada una de letras que se eligió.
apariciones = {}
for letra in letras:
    apariciones[letra] = texto.lower().count(letra)

#2- Cuantas palabras hay en total en todo el texto.
palabras = texto.split()
cantidad_palabras = len(palabras)

#3- Cual es la primera letra y cuál es la última. (Indexación)
primera_letra = texto[0]
ultima_letra = texto[-1]

#4- Mostrar el texto en orden inverso.
palabras = texto.split()

palabras_invertidas = palabras[::-1]

texto_invertido = " ".join(palabras_invertidas)

# mostrar resultados
print(f"Cantidad de veces que aparece cada letra:")
for letra, cantidad in apariciones.items():
    print(f"{letra}: {cantidad}")

print(f"Cantidad total de palabras: {cantidad_palabras}")

print(f"Primera letra: {primera_letra}")
print(f"Última letra: {ultima_letra}")

#5- Decir si la palabra "python" aparece en el texto.

for i in texto:
    if "python" in texto.lower():
        print("La palabra 'python' aparece en el texto")
        break
    else:
        print("La palabra 'python' no aparece en el texto")
        break

print("\n")