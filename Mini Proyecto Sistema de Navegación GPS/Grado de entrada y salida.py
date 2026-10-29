def calcular_grados(grafo):
    entrada = {nodo: 0 for nodo in grafo}
    salida = {nodo: len(vecinos) for nodo, vecinos in grafo.items()}

    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            if vecino not in entrada:
                entrada[vecino] = 0
                salida[vecino] = 0

            entrada[vecino] += 1

    for nodo in entrada:
        print(
            f"{nodo}: entrada = {entrada[nodo]}, "
            f"salida = {salida[nodo]}"
        )

grafo = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"],
    "D": ["C"]
}

calcular_grados(grafo)
