def subcadena_sin_repetidos(texto: str) -> int:
    posiciones = {}
    inicio = 0
    maximo = 0

    for fin in range(len(texto)):
        caracter = texto[fin]

        if caracter in posiciones and posiciones[caracter] >= inicio:
            inicio = posiciones[caracter] + 1

        posiciones[caracter] = fin

        longitud = fin - inicio + 1

        if longitud > maximo:
            maximo = longitud

    return maximo,posiciones

print(subcadena_sin_repetidos("abcabcbb"))
print(subcadena_sin_repetidos(""))
print(subcadena_sin_repetidos("hola mundo hola"))