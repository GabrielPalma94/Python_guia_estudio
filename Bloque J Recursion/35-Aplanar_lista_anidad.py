def aplanar_lista(datos:list):
    resultado = []
    for elemento in datos:
        if isinstance(elemento,list):
            resultado.extend(aplanar_lista(elemento))
        else:
            resultado.append(elemento)
    return resultado
print(aplanar_lista([1,[2,[3,4]],5]))
print(aplanar_lista([[],[[]]]))