lista=[]
n=None
while True:
    x = input("Ingrese un numero o 'fin' para terminar: ")
    if x == 'fin':
        break 
    y = int(x)
    lista.append(y)
i = 0
while i < len(lista):
    j=i+1
    while j < len(lista):
        if lista[i] == lista[j]:
            del lista[j]
        else:
            j +=1
    i +=1
print(lista)