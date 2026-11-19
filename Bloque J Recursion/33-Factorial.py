def factorial(n:int):
    if n < 0:
        return ValueError('No existen valores negativos')
    elif n == 0:
        return 1
    resultado = n * factorial(n-1)
    return resultado
print(factorial(5))
