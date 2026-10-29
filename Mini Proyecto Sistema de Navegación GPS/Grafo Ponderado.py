import heapq

def menor_latencia(grafo, inicio, destino):
    if inicio not in grafo or destino not in grafo:
        return None, float("inf")

    distancias = {n: float("inf") for n in grafo}
    anteriores = {n: None for n in grafo}

    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        latencia, actual = heapq.heappop(cola)

        if latencia > distancias[actual]:
            continue

        for vecino, peso in grafo[actual]:
            if peso < 0:
                raise ValueError("La latencia no puede ser negativa.")

            nueva = latencia + peso

            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                anteriores[vecino] = actual
                heapq.heappush(cola, (nueva, vecino))

    if distancias[destino] == float("inf"):
        return None, float("inf")

    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = anteriores[actual]

    camino.reverse()
    return camino, distancias[destino]


red = {
    "PC": [("Router", 5), ("ServidorA", 15)],
    "Router": [("PC", 5), ("ServidorA", 4),
               ("ServidorB", 10)],
    "ServidorA": [("PC", 15), ("Router", 4),
                  ("ServidorB", 3)],
    "ServidorB": [("Router", 10), ("ServidorA", 3)]
}

ruta, latencia = menor_latencia(red, "PC", "ServidorB")

if ruta:
    print("Ruta:", " -> ".join(ruta))
    print("Latencia total:", latencia, "ms")
else:
    print("No existe conexión entre los dispositivos.")
