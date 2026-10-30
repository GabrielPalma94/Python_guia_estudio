class Pila:
    def __init__(self):
        self.lista_numeros=[]

    def pedir_numeros(self):
        while True:
            x = input("Ingrese un valor o 'fin' para terminar:")
            if x == 'fin': 
                break 
            x = int(x)
            self.lista_numeros.append(x)

    def push(self,x):
        self.lista_numeros.append(x)
        return None

    def pop(self):
        if not self.lista_numeros:
            raise IndexError
        else:
            return self.lista_numeros.pop()

    def peek(self):
        if not self.lista_numeros:
            raise IndexError
        else:
            return self.lista_numeros[-1]
    
    def is_empty(self):
        if not self.lista_numeros:
            return True
        else:
            return False
    def size(self):
        return len(self.lista_numeros)

pila1 = Pila()
pila1.pedir_numeros()
print(pila1.peek())
print(pila1.size())