#9-Escribe un programa que pida al usuario un número y luego imprima la
#secuencia de Fibonacci correspondiente a ese número.
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("cuantos terminos? "))

# primeros dos terminos
n1, n2 = 0, 1
count = 0

# chequee si el numero de terminos es valido
if nterms <= 0:
   print("por favor ingrese un entero positivo")
# si solo hay un termino, retorne n1
elif nterms == 1:
   print("secuencia de Fibonacci hasta",nterms,":")
   print(n1)
# genera la secuencia de fibonacci
else:
   print("secuencia de Fibonacci:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1