x =int(input('Agregue el numero hasta cual quiere llegar \n'))
tup = []
for i in range(1,x+1):
    if i%3 == 0 and i%5 == 0:
        tup.append('FizzBuzz')
    elif i%3 == 0  and i%5 != 0:
        tup.append('Fizz')
    elif i%5 == 0 and i%3 != 0:
        tup.append('Buzz')
    else:
        tup.append(i)
for i in tup:
    print(i)
