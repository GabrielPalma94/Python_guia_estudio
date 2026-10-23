a = [10,20]
b = a
b.append(30)
b = [40,50]
print(a)  # Output: [10, 20, 30]
print(b)  # Output: [40, 50]
print(a is b)  # Output: False