lista1 = []
lista2 = []
while True:
    x = input("Ingrese un numero o 'fin' para terminar: ")
    lista1.append(x)
    if x == 'fin':
        break
lista1.remove('fin')
for c in lista1:
    if c not in lista2:
        lista2.append(c)
print(lista2)