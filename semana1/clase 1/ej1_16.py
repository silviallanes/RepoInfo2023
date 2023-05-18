##16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
##e imprima su índice de masa corporal (IMC).
##La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).
peso = float(input("Ingrese el peso: "))
altura = float(input("ingrese la altura: "))
IMC = peso / (altura ** 2)
print("El IMC es: ", IMC)