
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
def a_lista(cabeza:Nodo | None):
    resultado = []
    actual = cabeza 
    while actual is not None:
        resultado.append(actual.dato)
        actual = actual.siguiente
    return resultado
nodos = desde_lista([1,2,3,4])
print(a_lista(nodos))
print(desde_lista([]))