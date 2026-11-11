l1 =[]
l2 = []
ln=[]
l_ordenada = []
while True:
    try:
        x = input("Ingrese un número para la PRIMERA lista ('fin' para terminar): ")
        if x == 'fin':
            break
        y = int(x)
        l1.append(y)
    except ValueError:
        print("Por favor, ingrese un número válido o 'fin' para terminar.")
while True:
    try:
        x = input("Ingrese un número para la SEGUNDA lista ('fin' para terminar): ")
        if x == 'fin':
            break
        y = int(x)
        l2.append(y)
    except ValueError:
        print("Por favor, ingrese un número válido o 'fin' para terminar.")
ln = l1 + l2
n = len(ln)
for i in range(n):
    for j in range(0, n-i-1):
        if ln[j] > ln[j+1]:
            ln[j], ln[j+1] = ln[j+1], ln[j]
print("La lista combinada y ordenada es:", ln)