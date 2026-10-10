def contar_caminos(filas, columnas, fila=0, columna=0):
    # Caso base: llegamos al destino
    if fila == filas - 1 and columna == columnas - 1:
        return 1

    # Caso base: salimos de los límites
    if fila >= filas or columna >= columnas:
        return 0

    # Caso recursivo: mover hacia abajo
    abajo = contar_caminos(
        filas, columnas, fila + 1, columna
    )

    # Caso recursivo: mover hacia la derecha
    derecha = contar_caminos(
        filas, columnas, fila, columna + 1
    )

    return abajo + derecha


print(contar_caminos(3, 3))