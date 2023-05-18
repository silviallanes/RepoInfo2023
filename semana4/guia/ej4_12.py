'''12-Crea una función llamada convertir_temperatura que tome una temperatura
en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
es: Fahrenheit = (Celsius * 9/5) + 32.'''
def convertir_temperatura(celsius):
    return((celsius * 9/5) + 32)

temperatura = int(input("ingrese una temperatura en ºC: "))
print("la temperatura en Fahrenheit es de: ",convertir_temperatura(temperatura), " ºF")