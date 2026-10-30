def two_sum(numeros,objetivo):
    for i in range(len(numeros)):
        for j in range(i+1,len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                return (i,j)
    return None

