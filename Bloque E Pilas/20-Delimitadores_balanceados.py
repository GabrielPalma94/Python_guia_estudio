pila =[]
parejas ={')':'(',']':'[','}':'{' }

cadena = input('Ingrese el texto a analizar: ')
valido = True
for c in cadena:
    if c in '([{':
        pila.append(c)
    elif c in ')]}':
        if not pila:
            valido = False
            break
        u = pila.pop()
        if u != parejas[c]:
            valido = False
            break
if pila:
    valido = False
print(valido)
