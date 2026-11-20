from collections import deque
class NodoArbol():
    def __init__(self, valor:int,izquierdo:'NodoArbol|None'=None,derecho:'NodoArbol|None'=None):
        self.valor = valor
        self.derecha = derecho
        self.izquierda = izquierdo
def recorrido_niveles(raiz:NodoArbol|None):
    if raiz is None:
        return []
    cola = deque([raiz])
    resultado = []
    while cola:
        cantidad_nodos=len(cola)
        nivel = []
        for i in range(cantidad_nodos):
            nodo = cola.popleft()
            nivel.append(nodo.valor)
            if nodo.izquierda is not None:
                cola.append(nodo.izquierda)
            if nodo.derecha is not None:
                cola.append(nodo.derecha)
        resultado.append(nivel)
    return resultado
raiz = NodoArbol(500)
raiz.izquierda = NodoArbol(400)
raiz.derecha = NodoArbol(300)
raiz.izquierda.izquierda = NodoArbol(450)
raiz.izquierda.derecha = NodoArbol(430)
raiz.derecha.izquierda = NodoArbol(350)
raiz.derecha.derecha = NodoArbol(330)
print(recorrido_niveles(raiz))