x = int(input('Ingrese un numero para saber si es primo o no: '))
lista1 = []
lista2 = []
if x <= 1 :
    print(False)
else:
    for i in range(2,x+1):
        if i not in lista2:
            lista1.append(i)
            for j in range(i*i,x+1,i):
                lista2.append(j)        
if x in lista1:
    print(True)
else:
    print(False)
