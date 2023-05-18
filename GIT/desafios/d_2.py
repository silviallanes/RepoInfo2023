#desafio 3
import random
#Pedir al usuario que ingrese su nombre
nombre = input("ingrese su nombre: ")
#Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos
#para adivinarlo.
print(f"Bienvenido {nombre} el número para adivinar está entre 1 y 100 y tiene 8 intentos para adivinar ")
nro = random.randint(1,100)

intento = 1

while intento <= 8:
    nro_usuario = int(input("El número es?: "))
    if type(nro_usuario) == int:
        if nro_usuario == nro:
            print(f"Los numeros coinciden. Ha ganado en el intento nro {intento}")
            break
        elif nro_usuario < nro:
            print("El número a adivinar es mayor que ",nro_usuario)
        else: 
            print("El numero a adivinar es menor que ", nro_usuario)
        
        print("le quedan ", 8-intento)
        intento += 1
               
    else: 
        print("Error. debe ingresar un número entero. vuelva a intentarlo")     
if intento > 8:
    print("Se ha quedado sin intentos, el nro a adivinar es: ", nro)        
              
            
    
    

