cadena = input("Ingrese el texto a evaluar: ")
x = len(cadena)
if cadena == cadena[::-1]:
    print(True)
else:
    print(False)