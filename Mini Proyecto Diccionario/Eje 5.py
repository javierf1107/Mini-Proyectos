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

    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecho, resultado)

    def balancear_arbol(self):
        valores = self.inorden()
        nuevo_arbol = ArbolBinarioBusqueda()

        nuevo_arbol.raiz = self._construir_balanceado(
            valores, 0, len(valores) - 1
        )

        return nuevo_arbol

    def _construir_balanceado(self, valores, inicio, fin):
        if inicio > fin:
            return None

        medio = (inicio + fin) // 2
        nodo = NodoArbol(valores[medio])

        nodo.izquierdo = self._construir_balanceado(
            valores, inicio, medio - 1
        )

        nodo.derecho = self._construir_balanceado(
            valores, medio + 1, fin
        )

        return nodo

    def altura(self, nodo):
        if nodo is None:
            return -1

        return 1 + max(
            self.altura(nodo.izquierdo),
            self.altura(nodo.derecho)
        )


arbol = ArbolBinarioBusqueda()

for numero in [1, 2, 3, 4, 5, 6, 7]:
    arbol.insertar(numero)

print("Altura original:", arbol.altura(arbol.raiz))

arbol_balanceado = arbol.balancear_arbol()

print("Altura balanceada:", arbol_balanceado.altura(
    arbol_balanceado.raiz
))

print("Valores originales:", arbol.inorden())
print("Valores balanceados:", arbol_balanceado.inorden())
