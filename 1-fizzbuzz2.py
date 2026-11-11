lista=list()
n=0
try:
    n = int(input("Ingrese un número entero positivo: "))
except ValueError:
    print("Error: Debe ingresar un número entero positivo.")
if n < 1:
    print(lista)
else:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append("FizzBuzz")
        elif i % 3 == 0:
            lista.append("Fizz")
        elif i % 5 == 0:
            lista.append("Buzz")
        else:
            lista.append(i)
print(lista)