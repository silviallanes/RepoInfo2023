#silvia llanes
#Desafío 4: La inmobiliaria
import os
lista_Zona = ['A','B','C']  
valor_Estado = {'1': 'Disponible', '2':'Reservado', '3':'Vendido'}
Excluidos = {'año':2000, 'metros':60, 'habitaciones':2}
valor_Garaje = {'1': True,'0':False }

def imprimir_menu():
    print("Lista de opciones")
    print("1 - Agregar inmueble")
    print("2 - Eliminar inmueble")
    print("3 - Editar inmueble")
    print("4 - Modificar estado")
    print("5 - Filtrar por presupuesto")
    print("0 - Para Salir")
    
def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_lista_inmueble():#imprimir la lista actualizada, usada para: alta, baja
    i = 0
    while i < len(lista_inmueble): # Imprimir todos los elementos del diccionario
        print(i," -",lista_inmueble[i], end='\n')
        i += 1       
        
def validar_inmueble(inmueble): #usada para alta y edicion
    if inmueble['zona'] in lista_Zona:    
        if inmueble['año'] >= Excluidos['año']:
            if inmueble['metros'] >= Excluidos['metros']:
                if inmueble['habitaciones'] >= Excluidos['habitaciones']:
                    return True
                else:
                    print('No cumple con la cantidad de habitaciones')    
            else:
                print("No cumple con la cantidad de m2")
                return False
        else:
            print("No cumple con el año permitido")
            return False
    else:
        print("No es una zona habilitada")
        return False
    
def agregar_inmueble(lista, inmueble): #usada para alta
    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("Inmueble agregado con éxito")
        imprimir_lista_inmueble
 
def modificar_inmueble(lista, inmueble_nuevo, pos):
    if validar_inmueble(inmueble_nuevo):
        lista[pos]['año'] = inmueble_nuevo['año']
        lista[pos]['metros']= inmueble_nuevo['metros']
        lista[pos]['habitaciones'] = inmueble_nuevo['habitaciones']
        lista[pos]['garaje'] = inmueble_nuevo['garaje']
        lista[pos]['zona'] = inmueble_nuevo['zona']
        lista[pos]['estado'] = inmueble_nuevo['estado']
        print("El inmueble se ha actualizado exitosamente")
        imprimir_lista_inmueble()
    else:
        print("No se pudo modificar el inmueble")
   
#funcion ALTA Inmueble
def cargar_datos(): #alta
    diccionario = {}
    anio_alta = int(input("Ingrese el año: "))
    metros_alta = int(input("Ingrese los m2: "))
    habit_alta = int(input("Ingrese cantidad de habitaciones: "))
    garaje_alta = input("Ingrese si tiene o no Garage 1-True 0- False: ")
    zona_alta = input("ingrese la zona A - B o C: ").upper()
    estado_alta = input("Ingrese su estado 1- Disponible - 2-Reservado - 3- Vendido: ")
    diccionario = {'año': anio_alta,'metros': metros_alta,'habitaciones': habit_alta,'garaje': valor_Garaje[garaje_alta],'zona': zona_alta,'estado': valor_Estado[estado_alta]}
    return diccionario
            
#funcion BAJA Inmueble
def baja_inmueble(lista):
    borrar_pantalla()
    imprimir_lista_inmueble()
    indice = int(input("Seleccione el elemento de la lista a eliminar: "))
    # Buscar el elemento en la lista
    if indice >=0 and indice < len(lista):
        del lista[indice]
        print("Innueble borrado exitosamente!!")
        print("Lista resultante:")
        imprimir_lista_inmueble()
    else: 
        print("El elemento seleccionado no es válido")
     
#funcion MODIFICACION Inmueble

def editar_inmueble(lista):
    borrar_pantalla()
    imprimir_lista_inmueble() # Mostrar la lista para seleccionar el inmueble 
    indice = int(input("Seleccione el elemento de la lista a editar: "))
    # Buscar el elemento en la lista
    if indice >= 0 and indice < len(lista):
        print(lista[indice])
        inmueble_alta = cargar_datos()
        modificar_inmueble(lista,inmueble_alta, indice)
        
    else:
        print("Se ha seleccionado un valor no válido ")
    
#funcion modificacion Estado Inmueble
def modif_Estado(lista):
    borrar_pantalla()
    imprimir_lista_inmueble()
    indice = int(input("Seleccione el elemento de la lista a modificar su estado: "))
    if indice >=0 and indice < len(lista):
        estado_modif = int(input("Ingrese el estado a modificar 1-Disponible, 2: Reservado, 3: Vendido: "))
        if estado_modif != lista[indice]['estado'] and estado_modif >= 1 and estado_modif <= 3:
            lista[indice]['estado'] = valor_Estado[str(estado_modif)]
            print("Estado del inmueble cambiado exitosamente!!")
            print(lista[indice])
    else: 
        print("El elemento seleccionado no es válido")
   
     # Buscar el elemento en la lista
    
#busqueda de inmuebles segun presupuesto
def busqueda_inmueblexprecio(lista, presupuesto):
    borrar_pantalla()
    imprimir_lista_inmueble()
    inmueble_precio = {}
    lista_inmueble_precio = []
    
    for diccionario in lista:
        antiguedad = int(2023-diccionario['año'])
        precio_base = float(diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500) * (1 - antiguedad / 100)
        if diccionario['estado'] == 'Disponible' or diccionario['estado'] == 'Reservado':
            if diccionario['zona'] == 'A':
                precio = precio_base
            elif diccionario['zona'] == 'B':
                precio = precio_base * 1.5
            else:
                precio = precio_base * 2    
            if precio <= presupuesto:
                inmueble_precio = diccionario
                inmueble_precio['precio'] = precio
                lista_inmueble_precio.append(inmueble_precio)
                
    if len(lista_inmueble_precio) > 0:
        i = 0
        print("Los inmuebles que cumplen con el presupuesto indicado son:")
        while i < len(lista_inmueble_precio): # Imprimir todos los elementos del diccionario
            print(i," -",lista_inmueble_precio[i], end='\n')
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
imprimir_menu()
abm = int(input("Seleccionar una opción:  "))

while(abm != 0):
    if abm >= 1 and abm <= 5: 
        if abm == 1:
            print("Alta de inmueble")
            inmueble_alta = cargar_datos()
            agregar_inmueble(lista_inmueble, inmueble_alta)
        elif abm == 2: #baja
            baja_inmueble(lista_inmueble)
        elif abm == 3: #editar
            editar_inmueble(lista_inmueble)
        elif abm == 4: #modificar estado
            modif_Estado(lista_inmueble)
        elif abm == 5: #listar inmuebles por presupuesto
            presupuesto = float(input("Ingrese el presupuesto: "))
            busqueda_inmueblexprecio(lista_inmueble, presupuesto)
    else:
        print("Ingresó una opción no válida")
    print()   
    
    imprimir_menu()
    abm = int(input("Seleccionar una opción:  "))

print()
print("Ha salido correctamente")




