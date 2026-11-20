class NodoArbol():
    def __init__(self,valor:int,izquierdo: 'NodoArbol|None'=None,derecho:'NodoArbol|None' = None):
        self.valor = valor
        self.izquierda = izquierdo
        self.derecha = derecho
raiz = NodoArbol(50)
raiz.izquierda = NodoArbol(30)
raiz.izquierda.izquierda = NodoArbol(20)
raiz.izquierda.derecha = NodoArbol(40)
raiz.derecha = NodoArbol(70)
raiz.derecha.derecha = NodoArbol(90)

def altura(raiz:NodoArbol|None):
    if raiz is None:
        return 0
    altura_izquierda = altura(raiz.izquierda)
    altura_derecha = altura(raiz.derecha)
    return 1 + max(altura_izquierda,altura_derecha)
print(altura(raiz))

raiz2 = NodoArbol(100)
raiz2.izquierda = NodoArbol(90)
raiz2.derecha = NodoArbol(80)
raiz2.izquierda.izquierda = NodoArbol(70)
raiz2.izquierda.derecha = NodoArbol(60)
raiz2.izquierda.izquierda.izquierda = NodoArbol(50)
raiz2.izquierda.izquierda.derecha = NodoArbol(40)

print(altura(raiz2))
