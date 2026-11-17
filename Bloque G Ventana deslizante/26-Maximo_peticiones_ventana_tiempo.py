def max_peticiones_ventana(tiempos:list[int], segundos:int) -> int:
    if segundos <= 0:
        raise ValueError("Los segundos deben ser mayores que cero")
    izquierda = 0
    maximo = 0
    for derecha in range(len(tiempos)):
        while tiempos[derecha] - tiempos[izquierda] >= segundos:
            izquierda += 1
        cantidad = derecha - izquierda + 1
        maximo = max(maximo, cantidad)
    return(maximo)

print(max_peticiones_ventana([1, 2, 3, 10, 11], 3))
print(max_peticiones_ventana([1, 2, 3, 10, 11], 2))
print(max_peticiones_ventana([5,5,5], 1))
print(max_peticiones_ventana([],3))