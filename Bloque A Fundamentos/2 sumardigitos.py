num = int(input('Ingrese un numero para sumar sus digitos(No valen numeros negativos): '))
lista1 = []
while num > 0:
    x = num % 10
    lista1.append(x)
    num = num // 10 
lista2 = sum(lista1)
print('La suma de los digitos es: ', lista2)