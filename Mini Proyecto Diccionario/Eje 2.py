from collections import deque


class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def por_niveles(self):
        resultado = []

        if self.raiz is None:
            return resultado

        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)

            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)

            if nodo.derecho is not None:
                cola.append(nodo.derecho)

        return resultado


arbol = ArbolBinarioBusqueda()

for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(numero)

print("Recorrido por niveles:", arbol.por_niveles())
