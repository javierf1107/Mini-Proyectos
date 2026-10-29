import heapq

def dijkstra_camino(grafo, inicio, destino):
    if inicio not in grafo or destino not in grafo:
        return None, float("inf")

    distancias = {n: float("inf") for n in grafo}
    anteriores = {n: None for n in grafo}
    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:
        distancia, actual = heapq.heappop(cola)

        if distancia > distancias[actual]:
            continue

        if actual == destino:
            break

        for vecino, peso in grafo[actual]:
            if peso < 0:
                raise ValueError("No se permiten pesos negativos.")

            nueva = distancia + peso

            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                anteriores[vecino] = actual
                heapq.heappush(cola, (nueva, vecino))

    if distancias[destino] == float("inf"):
        return None, float("inf")

    camino = []
    nodo = destino

    while nodo is not None:
        camino.append(nodo)
        nodo = anteriores[nodo]

    camino.reverse()
    return camino, distancias[destino]


grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 5)],
    "C": [("A", 2), ("B", 1)],
    "D": [("B", 5), ("C", 8)]
}

camino, distancia = dijkstra_camino(grafo, "A", "D")

if camino:
    print("Camino exacto:", " -> ".join(camino))
    print("Distancia mínima:", distancia)
else:
    print("No existe un camino.")
