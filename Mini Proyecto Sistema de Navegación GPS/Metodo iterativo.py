def dfs_iterativo(grafo, inicio):
    if inicio not in grafo:
        return []

    visitados = set()
    pila = [inicio]
    resultado = []

    while pila:
        actual = pila.pop()

        if actual not in visitados:
            visitados.add(actual)
            resultado.append(actual)

            # Se invierte para conservar el orden
            # de vecinos de la lista original.
            for vecino in reversed(grafo[actual]):
                if vecino not in visitados:
                    pila.append(vecino)

    return resultado


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

print("Recorrido DFS:", dfs_iterativo(grafo, "A"))
