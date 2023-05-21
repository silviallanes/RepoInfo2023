import os

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False  # Verifica si la zona del inmueble es válida (A, B o C)
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False  # Verifica si el estado del inmueble es válido (Disponible, Reservado o Vendido)
    if inmueble['año'] < 2000 or inmueble['metros'] < 60 or inmueble['habitaciones'] < 2:
        return False  # Verifica si el año, los metros y las habitaciones del inmueble cumplen los requisitos mínimos
    return True  # Si todas las condiciones anteriores se cumplen, el inmueble es válido

def agregar_inmueble(lista_inmuebles, inmueble):
    if validar_inmueble(inmueble):
        lista_inmuebles.append(inmueble)  # Agrega el inmueble a la lista si cumple con las reglas de validación
        print("El inmueble ha sido agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def editar_inmueble(lista_inmuebles, indice, nuevo_inmueble):
    if validar_inmueble(nuevo_inmueble):
        if 0 <= indice < len(lista_inmuebles):
            lista_inmuebles[indice] = nuevo_inmueble  # Reemplaza el inmueble en el índice especificado por el nuevo inmueble
            print("El inmueble ha sido editado correctamente.")
        else:
            print("El índice del inmueble es inválido.")
    else:
        print("El inmueble no cumple con las reglas de validación.")

def eliminar_inmueble(lista_inmuebles, indice):
    if 0 <= indice < len(lista_inmuebles):
        del lista_inmuebles[indice]  # Elimina el inmueble en el índice especificado de la lista
        print("El inmueble ha sido eliminado correctamente.")
    else:
        print("El índice del inmueble es inválido.")

def cambiar_estado(lista_inmuebles, indice, nuevo_estado):
    if 0 <= indice < len(lista_inmuebles):
        lista_inmuebles[indice]['estado'] = nuevo_estado  # Cambia el estado del inmueble en el índice especificado por el nuevo estado
        print("El estado del inmueble ha sido cambiado correctamente.")
    else:
        print("El índice del inmueble es inválido.")

def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    inmuebles_encontrados = []  # Lista para almacenar los inmuebles encontrados
    for inmueble in lista_inmuebles:
        if (inmueble['estado'] in ['Disponible', 'Reservado'] and 
                calcular_precio_inmueble(inmueble) <= presupuesto):
            inmueble_con_precio = inmueble.copy()  # Realiza una copia del inmueble encontrado
            inmueble_con_precio['precio'] = calcular_precio_inmueble(inmueble)  # Calcula y agrega el precio al inmueble copiado
            inmuebles_encontrados.append(inmueble_con_precio)  # Agrega el inmueble copiado a la lista de inmuebles encontrados
    return inmuebles_encontrados

def calcular_precio_inmueble(inmueble):
    precio_base = inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500  # Calcula el precio base del inmueble según sus características
    antiguedad = 2023 - inmueble['año']  # Calcula la antigüedad del inmueble
    if inmueble['zona'] == 'A':
        return precio_base * (1 - antiguedad / 100)  # Calcula el precio final del inmueble para la zona A
    elif inmueble['zona'] == 'B':
        return precio_base * (1 - antiguedad / 100) * 1.5  # Calcula el precio final del inmueble para la zona B
    elif inmueble['zona'] == 'C':
        return precio_base * (1 - antiguedad / 100) * 2  # Calcula el precio final del inmueble para la zona C

def mostrar_inmueble(lista_inmuebles):
    for indice,inmueble in enumerate(lista_inmuebles):
         print (f"Inmueble, {indice}: {inmueble}")

lista_inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2012, 'metros': 120, 'habitaciones': 3, 'garaje': True, 'zona': 'A', 'estado': 'Reservado'},
    {'año': 2005, 'metros': 100, 'habitaciones': 2, 'garaje': True, 'zona': 'C', 'estado': 'Vendido'},
    {'año': 2018, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Disponible'},
    {'año': 2003, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Vendido'},
    {'año': 2019, 'metros': 70, 'habitaciones': 1, 'garaje': False, 'zona': 'B', 'estado': 'Disponible'},
    {'año': 2007, 'metros': 110, 'habitaciones': 3, 'garaje': True, 'zona': 'C', 'estado': 'Reservado'}
]

print("\n")

while True:
    
    mostrar_inmueble(lista_inmuebles)

    print("\n")
    
    comando = input("Ingrese una orden (1-agregar nuevo inmueble, 2-editar inmueble, 3-eliminar inmueble, 4-cambiar estado, 5-buscar por presupuesto, 6-salir): ")
    
    print("\n")

    if comando == "1":
        limpiar_pantalla()

        print("\n")

        inmueble = {} # Crear un diccionario para almacenar la información del inmueble
        inmueble['año'] = int(input("Ingrese el año del inmueble: ")) # Solicitar el año del inmueble al usuario
        inmueble['metros'] = int(input("Ingrese los metros del inmueble: ")) # Solicitar los metros del inmueble al usuario
        inmueble['habitaciones'] = int(input("Ingrese el número de habitaciones del inmueble: ")) # Solicitar el número de habitaciones al usuario
        inmueble['garaje'] = input("¿Tiene garaje? (S/N): ").lower() == "s" or "n" == False # Solicitar si el inmueble tiene garaje al usuario
        inmueble['zona'] = input("Ingrese la zona del inmueble (A, B o C): ").upper() # Solicitar la zona del inmueble al usuario
        
        estado_map = {"1": "Disponible", "2": "Reservado", "3": "Vendido"}  # Mapear los estados
        estado_input = input("Ingrese el estado del inmueble (1 'Disponible', 2 'Reservado' o 3 'Vendido'): ")
        inmueble['estado'] = estado_map.get(estado_input)  # Obtener el estado correspondiente del mapeo
        
        if validar_inmueble(inmueble): # Validar si el inmueble cumple con ciertas reglas de validación
            lista_inmuebles.append(inmueble)  # Agregar el inmueble a la lista de inmuebles existente
            print("El nuevo inmueble ha sido agregado.")
            print("Lista de inmuebles actualizada:")
        else:
            print("El inmueble no cumple con las reglas de validación.")
        
        print("\n")
        
    elif comando == "2":
        limpiar_pantalla()
        mostrar_inmueble(lista_inmuebles)
        
        print("\n")
        
        indice = int(input("Ingrese el índice del inmueble a editar: ")) # Solicitar al usuario el índice del inmueble a editar
        if 0 <= indice < len(lista_inmuebles): # Verificar si el índice está dentro del rango válido de la lista de inmuebles
            nuevo_inmueble = {} # Crear un diccionario para almacenar la información del nuevo inmueble
            nuevo_inmueble['año'] = int(input("Ingrese el nuevo año del inmueble: ")) # Solicitar al usuario el nuevo año del inmueble
            nuevo_inmueble['metros'] = int(input("Ingrese los nuevos metros del inmueble: ")) # Solicitar al usuario los nuevos metros del inmueble
            nuevo_inmueble['habitaciones'] = int(input("Ingrese el nuevo número de habitaciones del inmueble: ")) # Solicitar al usuario el nuevo número de habitaciones del inmueble
            nuevo_inmueble['garaje'] = input("¿Tiene garaje? (S/N): ").lower() == "s" or "n" == False # Solicitar al usuario si el nuevo inmueble tiene garaje (Sí/No)
            nuevo_inmueble['zona'] = input("Ingrese la nueva zona del inmueble (A, B o C): ").upper() # Solicitar al usuario la nueva zona del inmueble (A, B o C)
            
            estado_map = {"1": "Disponible", "2": "Reservado", "3": "Vendido"}  # Mapear los estados
            estado_input = input("Ingrese el estado del inmueble (1 'Disponible', 2 'Reservado' o 3 'Vendido'): ")
            nuevo_inmueble['estado'] = estado_map.get(estado_input)  # Obtener el estado correspondiente del mapeo

            if validar_inmueble(nuevo_inmueble): # Validar si el inmueble cumple con ciertas reglas de validación
                editar_inmueble(lista_inmuebles, indice, nuevo_inmueble) # Agregar el inmueble a la lista de inmuebles existente
                print("Lista de inmuebles actualizada:")
            else:
                print("El nuevo inmueble no cumple con las reglas de validación.")

        else:
            print("El índice del inmueble es inválido.")
        
        print("\n")

    elif comando == "3":
        limpiar_pantalla()
        mostrar_inmueble(lista_inmuebles)
        
        print("\n")
        
        indice = int(input("Ingrese el índice del inmueble a eliminar: ")) # Solicitar al usuario el índice del inmueble a eliminar
        if 0 <= indice < len(lista_inmuebles): # Verificar si el índice está dentro del rango válido de la lista de inmuebles
            eliminar_inmueble(lista_inmuebles, indice) # Llamar a la función 'eliminar_inmueble' para eliminar el inmueble correspondiente al índice dado
            print("Lista de inmuebles actualizada:")
        else:
            print("El índice del inmueble es inválido.")
        
        print("\n")

    elif comando == "4":
        limpiar_pantalla()
        mostrar_inmueble(lista_inmuebles)
        
        print("\n")
        
        indice = int(input("Ingrese el índice del inmueble a cambiar de estado: ")) # Solicitar al usuario el índice del inmueble al que se desea cambiar el estado
        if 0 <= indice < len(lista_inmuebles): # Verificar si el índice está dentro del rango válido de la lista de inmuebles
            estado_map = {"1": "Disponible", "2": "Reservado", "3": "Vendido"}  # Mapear los estados
            est = input("Ingrese el nuevo estado del inmueble (1 'Disponible', 2 'Reservado' o 3 'Vendido'): ") # Solicitar al usuario el nuevo estado del inmueble
            nuevo_estado = estado_map.get(est)  # Obtener el estado correspondiente del mapeo
            cambiar_estado(lista_inmuebles, indice, nuevo_estado) # Llamar a la función 'cambiar_estado' para cambiar el estado del inmueble correspondiente al índice dado
            print("Lista de inmuebles actualizada:")
        else:
            print("El índice del inmueble es inválido.")
        
        print("\n")

    elif comando == "5":
        limpiar_pantalla()
        presupuesto = float(input("Ingrese el presupuesto máximo: ")) # Solicitar al usuario el presupuesto máximo para la búsqueda
        inmuebles_encontrados = buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto) # Llamar a la función 'buscar_inmuebles_por_presupuesto' para obtener una lista de inmuebles que se ajusten al presupuesto dado
        print("Inmuebles encontrados:")
        for inmueble in inmuebles_encontrados: # Imprimir la lista de inmuebles encontrados
            print(inmueble)
        
        print("\n")

    elif comando == "6":
        break # Salir del bucle principal y finalizar el programa

    else:
        print("Orden no reconocida. Intente nuevamente.")
        
print("\n")

"""
INTEGRANTES:

Juan P. Diaz
Fernando Ferreyra
Jorge Lucas
Rafael Leguizamon
Bruno Zalazar
Valentina Portillo
Silvia Llanes
Nelida Ramirez
Julian Chavez
Federico Kliokis
lucas Nahuel Cárdenas

"""