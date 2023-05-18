# Juan Pablo Diaz, Zalazar Bruno Erwin, Portillo Valentina, Jorge Antonio Lucas, Rafael Marcelo Leguizamon, Llanes Silvia, Fernando Ferreyra

import random

print("\n")

# Pedimos al usuario que ingrese su nombre
nombre = input("¡Bienvenido! Por favor ingrese su nombre: ")

# Informamos al usuario sobre las reglas del juego
print("Hola " + nombre + ", el número a adivinar está entre 1 y 100, y tienes 8 intentos para adivinarlo.")

# Generamos un número aleatorio entre 1 y 100
numero_a_adivinar = random.randint(1, 100)

# Establecemos el número de intentos en 8
intentos_restantes = 8

# Comenzamos el bucle para permitir que el usuario adivine el número
while intentos_restantes > 0:
    # Informamos al usuario sobre los intentos restantes y le pedimos que ingrese un número
    print("Tienes " + str(intentos_restantes) + " intentos restantes.")
    numero_ingresado = input("Por favor ingrese un número entre 1 y 100: ")

    # Validamos si el usuario ingresó un número entero
    if not numero_ingresado.isdigit():
        print("Lo siento, debes ingresar un número entero.")
        print("")
        continue

    # Convertimos el número ingresado a entero
    numero_ingresado = int(numero_ingresado)

    # Comparamos el número ingresado con el número a adivinar
    if numero_ingresado < numero_a_adivinar:
        print("")
        print("El número a adivinar es mayor.")
        intentos_restantes -= 1

    elif numero_ingresado > numero_a_adivinar:
        print("")
        print("El número a adivinar es menor.")
        intentos_restantes -= 1
        
    else:
        print("")
        print("¡Felicitaciones " + nombre + "! Has adivinado el número en " + str(9 - intentos_restantes) + " intentos.")
        break

# Verificamos si el usuario agotó todos los intentos
if intentos_restantes == 0:
    print("Lo siento, has agotado tus 8 intentos. El número que debías adivinar era " + str(numero_a_adivinar) + ". ¡Mejor suerte la próxima vez!")

print("\n")