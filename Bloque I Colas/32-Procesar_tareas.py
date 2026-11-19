from collections import deque
def procesar_tareas(tareas:list[tuple[str,int]],turno:int):
    if turno <= 0:
        raise ValueError('El turno debe ser mayor a cero')
    cola = deque(tareas)
    terminadas = []
    while cola:
        nombre,duracion = cola.popleft()
        if duracion <= turno:
            terminadas.append(nombre)
        else:
            duracion -= turno
            cola.append((nombre,duracion))
    return terminadas
print(procesar_tareas([('a',3),('b',1),('c',2)],2))