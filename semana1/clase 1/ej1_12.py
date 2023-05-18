##12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
##dd/mm/aaaa y luego imprima su edad en años.
##Utiliza la función .split()

fecha = input("ingrese fecha de nacimiento dd/mm/aaaa: ")
fecha_split = fecha.split("/")
print(fecha_split)
edad = 2023 - int(fecha_split[2])
print("edad es: ", edad)