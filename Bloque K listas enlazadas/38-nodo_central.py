class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None
def nodo_central(cabeza:Nodo |None):
    lento = cabeza
    rapido = cabeza
    while rapido is not None and rapido.siguiente is not None:
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
    return lento
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
central = nodo_central(nodo1)
print(central.valor)