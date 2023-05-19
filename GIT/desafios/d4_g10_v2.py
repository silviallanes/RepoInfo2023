#silvia llanes
#Desafío 4: La inmobiliaria
import os
lista_Zona = ['A','B','C']  
valor_Estado = {'1': 'Disponible', '2':'Reservado', '3':'Vendido'}
Excluidos = {'año':2000, 'metros':60, 'habitaciones':2}
valor_Garaje = {'1': True,'0':False }

def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_inmueble(inmueble):
    if inmueble['zona'] in lista_Zona:    
        if inmueble['año'] >= Excluidos['año']:
            if inmueble['metros'] >= Excluidos['metros']:
                if inmueble['habitaciones'] >= Excluidos['habitaciones']:
                    lista_inmueble.append(inmueble)
                else:
                    print('No cumple con la cantidad de habitaciones')    
            else:
                print("No cumple con la cantidad de m2")
        else:
            print("No cumple con el año permitido")
    else:
        print("No es una zona habilitada")
    
def agregar_inmueble(lista, inmueble):
    if validar_inmueble(inmueble):
        lista.append(inmueble)

def modificar_inmueble(inmueble, inmueble_nuevo):
    if validar_inmueble(inmueble_nuevo):
        inmueble['año'] = inmueble_nuevo['año']
        inmueble['metros']= inmueble_nuevo['metros']
        inmueble['habitaciones'] = inmueble_nuevo['habitaciones']
        inmueble['garaje'] = inmueble_nuevo['garaje']
        inmueble['zona'] = inmueble_nuevo['zona']
        inmueble['estado'] = inmueble_nuevo['estado']
    

def imprimir_lista_inmueble():#imprimir la lista actualizada
    i = 0
    while i < len(lista_inmueble): # Imprimir todos los elementos del diccionario
        print(i," -",lista_inmueble[i], end='\n')
        i += 1             
#funcion ALTA Inmueble

def cargar_datos():
    anio_alta = int(input("Ingrese el año: "))
    metros_alta = int(input("Ingrese los m2: "))
    habit_alta = int(input("Ingrese cantidad de habitaciones: "))
    garaje_alta = input("Ingrese si tiene o no Garage 1-True 2- False: ")
    zona_alta = input("ingrese la zona A - B o C: ").upper()
    diccionario = {'año': anio_alta,'metros': metros_alta,'habitaciones': habit_alta,'garaje': valor_Garaje[garaje_alta],'zona': zona_alta,'estado': 'Disponible'}
    return diccionario
            
             
#funcion BAJA Inmueble
def baja_inmueble(lista):
    
    indice = int(input("Seleccione el elemento de la lista a eliminar: "))
    # Buscar el elemento en la lista
    if indice >=0 and indice < len(lista):
        del lista[indice]
    else: 
        print("El elemento seleccionado no es válido")
     
#funcion MODIFICACION Inmueble

def editar_inmueble():
    # Mostrar la lista para seleccionar el inmueble 
    imprimir_lista_inmueble()
    indice = int(input("Seleccione el elemento de la lista a editar: "))
    if indice >= 0 and indice < len(lista_inmueble):
        print(lista_inmueble[indice])
        
    else:
        print("Se ha seleccionado un valor no válido ")
    
#funcion modificacion Estado Inmueble
'''def modif_Estado(lista, estado):
    anio_modif = "2010"
    estado_modif = input("Ingrese el estado a modificar 1-Disponible, 2: Reservado, 3: Vendido: ")
    for diccionario in lista:
        if diccionario["año"] == anio_modif:
            diccionario["estado"] = valor_Estado[estado_modif]
            break
    else:
        print("Elemento no encontrado.")'''
   

#busqueda de inmuebles segun presupuesto
def busqueda_inmueblexprecio(lista, presupuesto):
    inmueble_precio = []

    for diccionario in lista:
        if diccionario['estado'] == 'Disponible' or diccionario['estado'] == 'Reservado':
            if diccionario['zona'] == 'A':
                precio = float(diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500) * (1 - 2023-diccionario['año'] / 100)
            elif diccionario['zona'] == 'B':
                precio = float(diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500) * (1 - 2023-diccionario['año'] / 100) * 1.5
            else:
                precio = float(diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500) * (1 - 2023-diccionario['año'] / 100) * 2    
            if precio <= presupuesto:
                inmueble_precio.append(diccionario)
                inmueble_precio['precio'].extend = float(precio)
    if len(inmueble_precio) > 0:
        i = 0
        while i < len(inmueble_precio): # Imprimir todos los elementos del diccionario
            print(i," -",inmueble_precio[i], end='\n')
            i += 1         
    else:
        print("No se encontraron inmuebles que cumplan con el presupuesto")
            
    
           
#Agregar, editar y eliminar inmuebles a la lista.
#Las funciones deben ajustarse al formato de lista y reglas de validación.

lista_inmueble = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
  
print("Imprimir la lista inicial: ")

imprimir_lista_inmueble()
print("Lista de opciones")
print("1 - Agregar inmueble")
print("2 - Eliminar inmueble")
print("3 - Editar inmueble")
print("4 - Modificar estado")
print("5 - Filtrar por presupuesto")
print("0 - Para Salir")
    
abm = int(input("Seleccionar una opción:  "))

while(abm != 0):
    if abm >= 1 and abm <= 5: 
        if abm == 1:
            print("Alta de inmueble")
            inmueble_alta = cargar_datos()
            agregar_inmueble(lista_inmueble, inmueble_alta)
        elif abm == 2: #baja
            borrar_pantalla()
            imprimir_lista_inmueble()
            baja_inmueble(lista_inmueble)
        elif abm == 3: #editar
            borrar_pantalla()
            imprimir_lista_inmueble()
            editar_inmueble()
        elif abm == 4: #modificar estado
            borrar_pantalla()
            imprimir_lista_inmueble()
            nuevoEstado = input("Ingrese nuevo estado: ")
            modif_Estado(lista_inmueble, nuevoEstado)
        elif abm == 5: #listar inmuebles por presupuesto
            borrar_pantalla()
            imprimir_lista_inmueble()
            presupuesto = float(input("Ingrese el presupuesto: "))
            busqueda_inmueblexprecio(lista_inmueble, presupuesto)
    else:
        print("Ingresó una opción no válida")
    print(" ")   
    print("Lista de opciones")
    print("1 - Agregar inmueble")
    print("2 - Eliminar inmueble")
    print("3 - Editar inmueble")
    print("4 - Modificar estado")
    print("5 - Filtrar por presupuesto")
    print("0 - Para Salir")
    
    abm = int(input("Seleccionar una opción:  "))






