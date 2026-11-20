from collections import deque
grafo = { 
    'api':['auth','pagos'],
    'auth':['db'],
    'pagos':['db','api'],
    'db':[]
}
def existe_camino(grafo:dict[str,list[str]],origen:str,destino:str):
    if origen not in grafo or destino not in grafo:
        raise ValueError('El origen o destino no existen en el grafo')
    if origen == destino:
        return True
    cola = deque([origen])
    visitados = {origen}
    while cola:
        actual =cola.popleft()
        for vecino in grafo[actual]:
            if vecino == destino:
                return True
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return False
print(existe_camino(grafo,'api','db'))
print(existe_camino(grafo,'db','api'))
print(existe_camino(grafo,'pagos','auth'))