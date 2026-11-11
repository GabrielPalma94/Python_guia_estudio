lista=[]
n= None
tup=()
m = None
while True:
    try:
        x = input("Introduzca un numero a la lista ('fin' para terminar): ")
        if x == 'fin':
            break
        y = int(x)
        lista.append(y)
    except ValueError:
        print('El valor introducido no es un numero')
while True:
    try:
        m = input('Introduzca un numero a buscar la suma en la lista: ')
        m = int(m)
        break
    except ValueError:
        print('El valor introducido no es un numero')
n=len(lista)
for i in range(n):
    for j in range(i+1,n):
        if lista[i]+lista[j] == m:
            tup = (i,j)
            break
    if tup:
        break
    else:
        tup = None
print('Los indices que suman ',m,' son: ',tup)