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
    
if len(lista) == 0:
    print(ValueError)
else:
    maximo = lista[0]
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    print("El numero maximo es: ", maximo)