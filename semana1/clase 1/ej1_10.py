##10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a
##euros. Supón que el tipo de cambio es de 0.84 euros por dólar.
cotizacion = 0.84
cifra = input("ingrese la cifra en dolares: ")
euros = float(cifra) * cotizacion
print("el monto resultante en euros es ", euros)