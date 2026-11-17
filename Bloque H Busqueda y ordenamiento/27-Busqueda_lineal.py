def busqueda_lineal(lista:list[int],objetivo:int):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice
print(busqueda_lineal([4,2,7,2],2))
print(busqueda_lineal([4,2],9))
