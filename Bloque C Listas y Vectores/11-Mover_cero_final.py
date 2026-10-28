lista = []
lista2 = []
z = 0
while True:
    x = input("Ingrese un numero o 'fin' para terminar: ")
    try:
        x = int(x)
        lista.append(x)
    except ValueError:
        print("Por favor, ingrese un numero o fin para terminar")
    if x == 'fin':
        break
if len(lista) == 0:
    print("Lista vacia")
else:
    for i in range(len(lista)):
        if lista[i] == 0:
            z +=1
lista2=[n for n in lista if n != 0]
for i in range(z):
    lista2.append(0)
print("La lista con los ceros al final es: ",lista2)