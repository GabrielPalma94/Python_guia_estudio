x = int(input('Ingrese un numero para saber si es primo o no: '))
z = x**(1/2)
y = z%1
lista1 = []
if x <= 1 :
    print(False)
elif y == 0:
    print(False)
else:
    for i in range(2,int(z)+1):
        for k in range(int(z),1,-1):
            if k%i == 0:
                pass
            else:
                if k not in lista1:
                    lista1.append(k)
                
print(lista1)
