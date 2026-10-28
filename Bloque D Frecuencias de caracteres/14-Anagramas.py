d1= {}
d2 ={}
cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")
for c in cadena1:
    if c not in d1:
        d1[c] = 1
    else:
        d1[c] +=1
for c in cadena2:
    if c not in d2:
        d2[c] =1
    else:
        d2[c] +=1
if d1 == d2:
    print(True)
else:
    print(False)