lista = []
d = {}

while True:
    x = input("Ingrese un numero o 'fin' para terminar: ")
    lista.append(x)
    if x == 'fin':
        break
for c in lista:
    if c not in d:
        d.update({c:1})        
    else:
        d[c] += 1
if all(d[c] ==1 for c in d):
    print(True,d)
else: 
    print(False,d)