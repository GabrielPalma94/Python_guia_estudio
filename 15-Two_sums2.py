lista=[]
a = None
tup = ()
while True:
    try:
        x = input('Introduzca un numero a la lista:')
        if x == 'fin':
            break
        y = int(x)
        lista.append(y)
    except ValueError:
        print('El valor introducido no es un numero')
while True:
    try:
        a = input('Introduzca un numero a buscar en la lista:')
        b = int(a)
        break
    except ValueError:
        print('El valor introducido no es un numero')
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] + lista[j] == b:
            tup=(lista[i], lista[j])
            break
    if tup:
        break

print('La lista introducida es:',tup)