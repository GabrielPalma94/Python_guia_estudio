cadena = input("Ingrese una cadena de texto: ")
z = 0
valor_espacio = True
for i in range(len(cadena)):
    if cadena[i].isspace() == False and valor_espacio == True:
        z = z +1
    valor_espacio = cadena[i].isspace()
print("La cantidad de palabras en la cadena es: ", z)