class Palabra:
    """Representa una palabra y su definicion."""

    def __init__(self, texto, definicion):
        self.texto = texto.strip()
        self.definicion = definicion.strip()


class Nodo:
    """Representa un nodo del arbol binario de busqueda."""

    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Almacena palabras ordenadas alfabeticamente."""

    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        """Inserta una palabra en el arbol."""
        if self.raiz is None:
            self.raiz = Nodo(palabra)
        else:
            self._insertar_recursivo(self.raiz, palabra)

    def _insertar_recursivo(self, nodo, palabra):
        texto_nuevo = palabra.texto.casefold()
        texto_actual = nodo.palabra.texto.casefold()

        if texto_nuevo < texto_actual:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(palabra)
            else:
                self._insertar_recursivo(nodo.izquierdo, palabra)

        elif texto_nuevo > texto_actual:
            if nodo.derecho is None:
                nodo.derecho = Nodo(palabra)
            else:
                self._insertar_recursivo(nodo.derecho, palabra)

        else:
            # Si existe, se actualiza su definicion.
            nodo.palabra.definicion = palabra.definicion

 