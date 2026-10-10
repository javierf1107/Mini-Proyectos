class ExploradorRecursivo:
   
    def imprimir_arbol(sistema, nivel=0):

        for nombre, contenido in sistema.items():

            # Creamos la indentación dependiendo del nivel.
            espacios = "    " * nivel
            
            if isinstance(contenido, dict):

                print(espacios + "[CARPETA] " + nombre)

                ExploradorRecursivo.imprimir_arbol(
                    contenido,
                    nivel + 1
                )
            else:
                print(espacios + "- " + nombre)


    def buscar_archivo(sistema, nombre, ruta=""):

        for nombre_elemento, contenido in sistema.items():

            if ruta == "":
                ruta_actual = nombre_elemento
            else:
                ruta_actual = ruta + "/" + nombre_elemento  
            if not isinstance(contenido, dict):

                if nombre_elemento == nombre:
                    return ruta_actual
            else:
                resultado = ExploradorRecursivo.buscar_archivo(
                    contenido,
                    nombre,
                    ruta_actual
                )
                if resultado is not None:
                    return resultado
        return None


    def contar_archivos(sistema):

        contador = 0

        # Recorremos cada elemento.
        for nombre, contenido in sistema.items():

            if not isinstance(contenido, dict):
                contador += 1
            else:
                contador += ExploradorRecursivo.contar_archivos(
                    contenido
                )
        return contador


# --------------------------------------------------
# SISTEMA DE ARCHIVOS DE EJEMPLO
# --------------------------------------------------

sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "tareas": {
            "recursividad.py": "5kb",
            "base_datos.sql": "20kb"
        },
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },

    "Descargas": {
        "programa.exe": "15mb",
        "manual.pdf": "3mb"
    },

    "sistema.dll": "500kb"
}


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

print("======================================")
print("     EXPLORADOR RECURSIVO             ")
print("======================================")

print("\n1. ESTRUCTURA DEL SISTEMA DE ARCHIVOS")
print("--------------------------------------")

ExploradorRecursivo.imprimir_arbol(sistema_archivos)


print("\n2. BÚSQUEDA DE ARCHIVOS")
print("--------------------------------------")

archivo_buscado = "recursividad.py"

resultado = ExploradorRecursivo.buscar_archivo(
    sistema_archivos,
    archivo_buscado
)

if resultado is not None:
    print("Archivo encontrado:", resultado)
else:
    print("Archivo no encontrado.")


print("\n3. CANTIDAD TOTAL DE ARCHIVOS")
print("--------------------------------------")

total = ExploradorRecursivo.contar_archivos(
    sistema_archivos
)

print("Total de archivos:", total)