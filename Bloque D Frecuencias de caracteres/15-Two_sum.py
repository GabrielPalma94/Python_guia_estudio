def two_sum(numeros,objetivo):
    for i in range(len(numeros)):
        for j in range(i+1,len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                return (i,j)
    return None


x=two_sum([1,2,3,4,5,6,7,8,9],8)
print(x)