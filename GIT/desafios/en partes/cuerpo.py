#silvia llanes
#Desafío 4: La inmobiliaria
from funciones_inmuebles import *
import os

# reglas a seguir
lista_Zona = ['A','B','C']  
valor_Estado = {'1': 'Disponible', '2':'Reservado', '3':'Vendido'}
Excluidos = {'año':2000, 'metros':60, 'habitaciones':2}
valor_Garaje = {'1': True,'0':False }

def borrar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
 
         
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






