lista = []
while True:
    x = input("Ingrese un numero o 'fin' para terminar: ")
    try:
        x = int(x)
        lista.append(x)
    except ValueError:
        print("Por favor, ingrese un numero o fin para terminar")
    if x == 'fin':
        break

lista_invertida = []
for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])

print("La lista invertida es: ", lista_invertida)