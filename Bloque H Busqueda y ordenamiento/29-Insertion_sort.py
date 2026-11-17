def insertion_sort(lista:list):
    for i in range(len(lista)):
        for j in range(1,len(lista)):
            if lista[j] < lista[j-1]:
                lista[j],lista[j-1] = lista[j-1],lista[j]
    return lista

print(insertion_sort([5,4,3,2,1]))
print(insertion_sort([]))
print(insertion_sort([1,-3,2,-5,0]))
print(insertion_sort([1,2,2,3,3,1]))