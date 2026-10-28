d = {}
cadena = input("Ingresa la cadena a analizar: ")
for c in cadena:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(d)