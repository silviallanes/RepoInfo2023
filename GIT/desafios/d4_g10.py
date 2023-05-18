#silvia llanes
#Desafío 4: La inmobiliaria
'''Reglas de validacion'''
lista_Zona = ['A','B','C']  
valor_Estado = {'1': 'Disponible', '2':'Reservado', '3':'Vendido'}
Excluidos = {'año':1999, 'metros':59, 'habitaciones':1}
valor_Garaje = {'1': True,'0':False }
'''Reglas de precio
Reglas de precio
Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2
'''
#funciones--------
#funcion ALTA Inmueble
def alta_inmueble(lista):
    diccionario = {}
    anio_alta = int(input("Ingrese el año: "))
    metros_alta = int(input("Ingrese los m2: "))
    habit_alta = int(input("Ingrese cantidad de habitaciones: "))
    garaje_alta = input("Ingrese si tiene o no Garage 1-True 2- False: ")
    zona_alta = input("ingrese la zona A - B o C: ")
                
    if zona_alta in lista_Zona:    
        if anio_alta > Excluidos['año']:
            if metros_alta > Excluidos['metros']:
                if habit_alta > Excluidos['habitaciones']:
                    
                    diccionario = {'año': anio_alta,'metros': metros_alta,'habitaciones': habit_alta,'garaje': valor_Garaje[garaje_alta],'zona': zona_alta,'estado': 'Disponible'}
                    lista.append(diccionario)
                else:
                    print('No cumple con la cantidad de habitaciones')    
            else:
                print("No cumple con la cantidad de m2")
        else:
            print("No cumple con el año permitido")
    else:
        print("No es una zona habilitada")

                        
#funcion BAJA Inmueble
def baja_inmueble(lista):
    print("lista de inmuebles: ",lista_inmueble)
    # Elemento a buscar
    anio_baja = "2016"

    # Buscar el elemento en la lista
    for diccionario in lista:
        if diccionario["año"] == anio_baja:
            print("Elemento encontrado:", diccionario)
            del diccionario
            break
    else:
        print("Elemento no encontrado.")
    print(lista)
     
#funcion MODIFICAION Inmueble

#funcion modificacion Estado Inmueble
def modif_Estado(lista, estado):
    anio_modif = "2010"
    estado_modif = input("Ingrese el estado a modificar 1-Disponible, 2: Reservado, 3: Vendido: ")
    for diccionario in lista:
        if diccionario["año"] == anio_modif:
            diccionario["estado"] = valor_Estado[estado_modif]
            break
    else:
        print("Elemento no encontrado.")
    print(lista)

#busqueda de inmuebles segun presupuesto
def busqueda_inmueblexprecio(lista, presupuesto):
    inmueble_precio = []
    i = 0
    for diccionario in lista:
        if diccionario['Estado'] == "Disponible" or diccionario['Estado'] == "Reservado":
            if diccionario['zona'] == 'A':
                precio = (diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500) * (1 - 2023-diccionario['año'] / 100)
            elif diccionario['zona'] == 'B':
                precio = (diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500) * (1 - 2023-diccionario['año'] / 100) * 1.5
            else:
                precio = (diccionario['metros'] * 100 + diccionario['habitaciones'] * 500 + diccionario['garaje'] * 1500) * (1 - 2023-diccionario['año'] / 100) * 2    
            if precio <= presupuesto:
                inmueble_precio.append(diccionario)
                inmueble_precio.extend(precio)
            
        
           
#Agregar, editar y eliminar inmuebles a la lista.
#Las funciones deben ajustarse al formato de lista y reglas de validación.

lista_inmueble = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
print(lista_inmueble)
# Imprimir todos los elementos del diccionario
abm = int(input("Seleccionar una opción: 1-Alta, 2-Baja, 3-Edicion, 0-Salir: "))
print("Imprimir la lista inicial: ")
print(lista_inmueble)
while(abm !=0):
    if abm >= 1 and abm <= 3: 
        if abm == 1: 
            alta_inmueble(lista_inmueble)
        elif abm == 2: 
            baja_inmueble(lista_inmueble)
    else:
        print("Ingresó una opción no válida")
    print(lista_inmueble)
    abm = int(input("Seleccionar una opción: 1-Alta, 2-Baja, 3-Edicion, 0-Salir "))
print(lista_inmueble)

#-Cambiar el estado de un inmueble, sin modificar sus demás datos.
nuevoEstado = input("Ingrese nuevo estado: ")
modif_Estado(lista_inmueble, nuevoEstado)

#busqueda de inmuebles segun un presupuesto dado
presupuesto = float(input("Ingrese el presupuesto: "))
busqueda_inmueblexprecio(lista_inmueble, presupuesto)

