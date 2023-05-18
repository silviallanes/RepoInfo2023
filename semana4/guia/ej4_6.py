'''6-Crea una función llamada es_par que tome un número como parámetro y
devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
devuelva Es impar o No es par.'''
def es_par(nro):
    return (nro % 2 == 0)

a = input("ingrese un valor para determinar si es par: ")
if a.isdigit():
    z = int(a)
    if (es_par(z)):
        print(f"{z} es par")
    else:
        print(f"{z} no es par")
else:
    print(f"{a} no es un número")