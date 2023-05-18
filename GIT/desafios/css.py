texto = input("agregar texto")
letters =input("agregar tres letras")
q_letters = {}

for letter in letters:
    q_letters[letter] = texto.lower().count(letter)

print ("apariciones de letras:")

for letter, cant in q_letters.items():
    print (f"{letter} -> {cant}") 