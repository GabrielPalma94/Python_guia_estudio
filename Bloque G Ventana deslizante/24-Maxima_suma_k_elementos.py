lista=[]
max_suma = float('-inf')
i = 0
while True:
    try:
        x = input("Ingrese un numero a la lista o 'fin' para terminar: ")
        if x == 'fin':
            break 
        y = int(x)
        lista.append(y)
    except ValueError:
        print("Por favor, ingrese un numero valido.")
while True:
    try:
        k = int(input("Ingrese el valor de k: "))
        break
    except ValueError:
        print("Por favor, ingrese un numero valido.")
if k <= 0 or k > len(lista):
    print(ValueError)
else:
    while i+k<= len(lista):
        suma = sum(lista[i:i+k])
        if suma > max_suma:
            max_suma = suma
        i += 1
print(max_suma)