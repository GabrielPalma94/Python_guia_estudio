class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
def desde_lista(valores:list[int]):
    cabeza = None
    actual = None
    for valor in valores:
        nuevo = Nodo(valor)
        if cabeza is None:
            cabeza = nuevo
        else:
            actual.siguiente = nuevo
        actual = nuevo
    return cabeza
def tiene_ciclo(cabeza: Nodo |None):
    lento = cabeza 
    rapido = cabeza
    while rapido is not None and rapido.siguiente is not None:
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
        if lento is rapido:
            return True
    return False

nodos = desde_lista([1,2,3,4,5])
print(tiene_ciclo(nodos))

segundo = nodos.siguiente
ultimo = nodos
while ultimo.siguiente is not None:
    ultimo = ultimo.siguiente
ultimo.siguiente=segundo

print(tiene_ciclo(nodos))