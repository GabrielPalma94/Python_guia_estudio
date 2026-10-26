cadena = input("Ingrese el texto a evaluar: ")
vocales = ['a','e','i','o','u','A','E','I','O','U']
z = 0
for x in cadena:
    if x in vocales:
        z +=1
print(z)