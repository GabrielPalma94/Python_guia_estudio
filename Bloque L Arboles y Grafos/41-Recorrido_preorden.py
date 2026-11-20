class NodoArbol():
    def __init__(self,valor:int,izquierdo: 'NodoArbol | None'=None,derecho:'NodoArbol|None'=None):
        self.valor = valor
        self.izquierda = izquierdo
        self.derecha = derecho
def preorden(raiz:NodoArbol|None):
    resultado = []
    if raiz is None:
        return resultado
    resultado.append(raiz.valor)
    resultado.extend(preorden(raiz.izquierda))
    resultado.extend(preorden(raiz.derecha))
    return resultado
raiz = NodoArbol(50)
raiz.izquierda = NodoArbol(30)
raiz.derecha = NodoArbol(70)
raiz.izquierda.izquierda = NodoArbol(20)
raiz.izquierda.derecha = NodoArbol(40)
raiz.derecha.izquierda = NodoArbol(60)
raiz.derecha.derecha = NodoArbol(80)

print(preorden(raiz))