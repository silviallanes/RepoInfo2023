'''9-Crea una función llamada promedio que tome una lista de números como
parámetro y devuelva el promedio de esos números.'''
def promedio(lista_nros):

    return(sum(lista_nros)/len(lista_nros))

lista = [2,5,6,8,79,12,23,5]
print(lista)
print("el promedio de la lista de valores ingresados es ", promedio(lista))