def tiene_ciclo_dirigido(grafo):
    estado = {nodo: 0 for nodo in grafo}

    def dfs(nodo):
        estado[nodo] = 1

        for vecino in grafo[nodo]:
            if estado[vecino] == 1:
                return True

            if estado[vecino] == 0:
                if dfs(vecino):
                    return True

        estado[nodo] = 2
        return False

    for nodo in grafo:
        if estado[nodo] == 0:
            if dfs(nodo):
                return True

    return False

grafo1 = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

grafo2 = {
    "A": ["B"],
    "B": ["C"],
    "C": []
}

print("Grafo 1 tiene ciclo:", tiene_ciclo_dirigido(grafo1))
print("Grafo 2 tiene ciclo:", tiene_ciclo_dirigido(grafo2))
