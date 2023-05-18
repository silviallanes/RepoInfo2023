#ej1
texto = input("agregar texto: ")
letters = input("ingresar tres letras: ").lower()

q_letters = {}
for letter in letters:
   q_letters[letter] = texto.lower().count(letter)
  
for letter, cant in q_letters.items():
      print(f"la {letter} tiene -> {cant} ocurrencias")
