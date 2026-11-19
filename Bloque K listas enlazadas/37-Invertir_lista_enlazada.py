class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None
def invertir_enlazada(cabeza:Nodo |None):
    anterior = None
    actual = cabeza
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
    return anterior
nodo1=Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)
nodo4 = Nodo(40)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
cabeza = nodo1
def imprimir_lista(cabeza):
    actual = cabeza
    while actual is not None:
        print(actual.valor, end='->')
        actual = actual.siguiente
    print('None')
print('Lista original')
imprimir_lista(cabeza)
nueva_cabeza=invertir_enlazada(cabeza)
print('lista invertida')
imprimir_lista(nueva_cabeza)