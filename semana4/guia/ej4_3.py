'''3-Crea una función llamada invertir_cadena que tome una cadena de texto como
parámetro y devuelva la cadena invertida'''
def cadenainv(cadena):
    print("la cadena invertida es: ",cadena[::-1])
    
texto = input("ingrese una cadena a invertir:") 
cadenainv(texto)