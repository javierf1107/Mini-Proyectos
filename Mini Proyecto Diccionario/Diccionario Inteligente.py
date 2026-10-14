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

    def buscar_exacta(self, texto):
        """Busca una palabra completa en el arbol."""
        nodo = self.raiz
        texto = texto.strip().casefold()

        while nodo is not None:
            actual = nodo.palabra.texto.casefold()

            if texto == actual:
                return nodo.palabra
            elif texto < actual:
                nodo = nodo.izquierdo
            else:
                nodo = nodo.derecho

        return None

    def buscar_por_prefijo(self, prefijo):
        """Retorna las palabras que comienzan con el prefijo."""
        resultados = []
        prefijo = prefijo.strip().casefold()

        self._buscar_prefijo_recursivo(
            self.raiz, prefijo, resultados
        )

        return resultados

    def _buscar_prefijo_recursivo(self, nodo, prefijo, resultados):
        if nodo is None:
            return

        # Recorrido inorden para obtener resultados ordenados.
        self._buscar_prefijo_recursivo(
            nodo.izquierdo, prefijo, resultados
        )

        texto = nodo.palabra.texto.casefold()

        if texto.startswith(prefijo):
            resultados.append(nodo.palabra)

        self._buscar_prefijo_recursivo(
            nodo.derecho, prefijo, resultados
        )

    def obtener_todos(self):
        """Retorna todas las palabras en orden alfabetico."""
        palabras = []
        self._obtener_todos_recursivo(self.raiz, palabras)
        return palabras

    def _obtener_todos_recursivo(self, nodo, palabras):
        if nodo is not None:
            self._obtener_todos_recursivo(
                nodo.izquierdo, palabras
            )
            palabras.append(nodo.palabra)
            self._obtener_todos_recursivo(
                nodo.derecho, palabras
            )


def cargar_diccionario(arbol):
    """Carga las palabras iniciales en el arbol."""
    palabras = [
        ("algoritmo", "Conjunto de pasos para resolver un problema."),
        ("almacenamiento", "Proceso de guardar informacion."),
        ("analisis", "Estudio detallado de un tema."),
        ("aplicacion", "Programa informatico que realiza tareas."),
        ("archivo", "Conjunto de datos guardados."),
        ("arbol", "Estructura de datos formada por nodos."),
        ("arreglo", "Coleccion de elementos organizados."),
        ("atributo", "Caracteristica de un objeto."),
        ("autenticacion", "Proceso de verificar una identidad."),
        ("autocompletar", "Sugerir palabras mientras se escribe."),
        ("autonomia", "Capacidad de actuar independientemente."),
        ("aurora", "Luz que aparece antes de la salida del sol."),
        ("automata", "Modelo matematico de computacion."),
        ("base de datos", "Coleccion organizada de informacion."),
        ("binario", "Sistema que utiliza dos valores."),
        ("bit", "Unidad minima de informacion digital."),
        ("booleano", "Tipo de dato con valores verdadero o falso."),
        ("busqueda", "Proceso de localizar informacion."),
        ("byte", "Unidad de informacion formada por ocho bits."),
        ("cadena", "Secuencia de caracteres."),
        ("caracter", "Simbolo que forma parte de un texto."),
        ("ciclo", "Estructura que repite instrucciones."),
        ("clave", "Dato utilizado para identificar o acceder."),
        ("codigo", "Instrucciones escritas en un lenguaje."),
        ("compilador", "Programa que traduce codigo fuente."),
        ("computadora", "Dispositivo electronico que procesa datos."),
        ("condicion", "Expresion que permite tomar decisiones."),
        ("consola", "Interfaz de texto para interactuar con un programa."),
        ("contraseña", "Secreto utilizado para autenticar un usuario."),
        ("dato", "Representacion de un hecho o valor."),
        ("definicion", "Explicacion del significado de una palabra."),
        ("diccionario", "Coleccion de palabras y sus significados."),
        ("digital", "Relacionado con datos representados electronicamente."),
        ("entrada", "Informacion que recibe un programa."),
        ("estructura", "Forma en que se organizan los datos."),
        ("etiqueta", "Texto que identifica un elemento."),
        ("expresion", "Combinacion de valores y operadores."),
        ("funcion", "Bloque de codigo que realiza una tarea."),
        ("gestor", "Sistema que administra recursos o informacion."),
        ("informacion", "Datos organizados con significado."),
        ("interfaz", "Medio de comunicacion entre usuario y sistema."),
        ("iteracion", "Repeticion de un proceso."),
        ("lenguaje", "Sistema de simbolos para comunicarse."),
        ("lista", "Coleccion ordenada de elementos."),
        ("memoria", "Espacio donde se almacenan datos temporalmente."),
        ("metodo", "Funcion definida dentro de una clase."),
        ("nodo", "Elemento que almacena datos en una estructura."),
        ("objeto", "Instancia de una clase."),
        ("ordenamiento", "Proceso de organizar elementos."),
        ("palabra", "Unidad del lenguaje con significado."),
        ("programa", "Conjunto de instrucciones ejecutables."),
        ("programacion", "Actividad de crear programas informaticos."),
        ("prefijo", "Parte inicial de una palabra."),
        ("proceso", "Conjunto de acciones relacionadas."),
        ("recorrido", "Visita ordenada de los elementos de una estructura."),
        ("recursividad", "Tecnica donde una funcion se llama a si misma."),
        ("registro", "Conjunto de datos relacionados."),
        ("resultado", "Salida producida por una operacion."),
        ("raiz", "Nodo inicial de un arbol."),
        ("seguridad", "Proteccion de datos y sistemas."),
        ("servidor", "Sistema que ofrece servicios a otros equipos."),
        ("sistema", "Conjunto de componentes relacionados."),
        ("software", "Programas y aplicaciones informaticas."),
        ("texto", "Conjunto de caracteres que forman un contenido."),
        ("usuario", "Persona que utiliza un sistema."),
        ("variable", "Espacio identificado que almacena un valor."),
        ("verificacion", "Comprobacion de que algo es correcto."),
        ("web", "Sistema de documentos y recursos conectados."),
        ("red", "Conjunto de dispositivos conectados."),
        ("teclado", "Dispositivo utilizado para introducir texto."),
    ]

    for texto, definicion in palabras:
        arbol.insertar(Palabra(texto, definicion))


def mostrar_palabra(palabra):
    """Muestra una palabra y su definicion."""
    print(f"\nPalabra: {palabra.texto}")
    print(f"Definicion: {palabra.definicion}")


def mostrar_menu():
    """Presenta las opciones disponibles."""
    print("\n" + "=" * 40)
    print("       DICCIONARIO INTELIGENTE")
    print("=" * 40)
    print("1. Buscar palabra exacta")
    print("2. Autocompletar por prefijo")
    print("3. Ver diccionario completo")
    print("4. Salir")
    print("=" * 40)


def main():
    """Controla la ejecucion del programa."""
    arbol = ArbolBinarioBusqueda()
    cargar_diccionario(arbol)

    print("Bienvenido al Diccionario Inteligente.")
    print(f"Palabras cargadas: {len(arbol.obtener_todos())}")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            texto = input("Escriba la palabra que busca: ").strip()

            if not texto:
                print("Debe escribir una palabra.")
                continue

            palabra = arbol.buscar_exacta(texto)

            if palabra is not None:
                mostrar_palabra(palabra)
            else:
                print("La palabra no se encuentra en el diccionario.")

        elif opcion == "2":
            prefijo = input("Escriba el prefijo: ").strip()

            if not prefijo:
                print("Debe escribir un prefijo.")
                continue

            resultados = arbol.buscar_por_prefijo(prefijo)

            if resultados:
                print("\nPalabras encontradas:")
                for palabra in resultados:
                    print(f"- {palabra.texto}: {palabra.definicion}")
                print(f"\nTotal de coincidencias: {len(resultados)}")
            else:
                print("No se encontraron palabras con ese prefijo.")

        elif opcion == "3":
            palabras = arbol.obtener_todos()

            print("\nDICCIONARIO COMPLETO")
            print("-" * 40)

            for palabra in palabras:
                print(f"{palabra.texto}: {palabra.definicion}")

            print(f"\nTotal de palabras: {len(palabras)}")

        elif opcion == "4":
            print("Gracias por utilizar el Diccionario Inteligente.")
            break

        else:
            print("Opcion no valida. Seleccione del 1 al 4.")


if __name__ == "__main__":
    main()