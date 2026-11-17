def ordenar_usuarios(usuarios:list[dict]):
    lista_ordenada = sorted(usuarios, key=lambda item:(item['edad'],item['nombre']))
    return lista_ordenada
print(ordenar_usuarios([{"nombre": "Luis", "edad": 30}, {"nombre": "Ana", "edad": 30}, {"nombre": "Eva", "edad": 22}]))
      