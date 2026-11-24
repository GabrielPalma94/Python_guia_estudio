def suma_recursiva_lista(numeros:list[int],inicio:int=0):
    if inicio >= len(numeros):
        return 0
    return numeros[inicio] + suma_recursiva_lista(numeros,inicio+1)
print(suma_recursiva_lista([1,2,3,4]))