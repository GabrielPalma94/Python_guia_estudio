def busqueda_binaria(lista: list, objetivo: int):
    for j in range(len(lista)):
        if lista[j] == objetivo:
            return j 
print(busqueda_binaria([1, 2, 3, 4, 5], 3))
print(busqueda_binaria([1,3,5,7,9],7))
print(busqueda_binaria([1,3,5],4))
print(busqueda_binaria([],3))
print(busqueda_binaria([1,3,5,7,1],1))