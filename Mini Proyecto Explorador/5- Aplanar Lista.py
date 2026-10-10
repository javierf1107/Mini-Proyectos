def aplanar_lista(lista):
    resultado = []

    for elemento in lista:
        # Caso recursivo
        if isinstance(elemento, list):
            resultado.extend(aplanar_lista(elemento))
        else:
            # Caso base: elemento individual
            resultado.append(elemento)

    return resultado


print(aplanar_lista([1, [2, [3, 4], 5]]))