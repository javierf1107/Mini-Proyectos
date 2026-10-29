import heapq

class SistemaGPS:
    def __init__(self):
        # Cada ciudad tiene una lista de rutas y tiempos.
        self.grafo = {}

    def agregar_ciudad(self, ciudad):
        ciudad = ciudad.strip()

        if not ciudad:
            raise ValueError("El nombre de la ciudad no puede estar vacío.")

        if ciudad in self.grafo:
            raise ValueError("Esta ciudad ya existe.")

        self.grafo[ciudad] = []
        print("Ciudad agregada correctamente.")

    def agregar_ruta(self, origen, destino, minutos):
        origen = origen.strip()
        destino = destino.strip()

        if origen not in self.grafo:
            raise ValueError("La ciudad de origen no existe.")

        if destino not in self.grafo:
            raise ValueError("La ciudad de destino no existe.")

        if origen == destino:
            raise ValueError("Una ruta debe conectar ciudades diferentes.")

        if minutos <= 0:
            raise ValueError("El tiempo debe ser mayor que cero.")

        # Comprobar si la ruta ya existe.
        for vecino, tiempo in self.grafo[origen]:
            if vecino == destino:
                raise ValueError("Esta ruta ya está registrada.")

        # Las carreteras permiten viajar en ambos sentidos.
        self.grafo[origen].append((destino, minutos))
        self.grafo[destino].append((origen, minutos))

        print("Ruta agregada correctamente.")

    def mostrar_ciudades(self):
        if not self.grafo:
            print("No hay ciudades registradas.")
            return

        print("\n--- CIUDADES REGISTRADAS ---")

        for ciudad in self.grafo:
            print("-", ciudad)

    def mostrar_rutas(self):
        if not self.grafo:
            print("No hay rutas registradas.")
            return

        print("\n--- RUTAS REGISTRADAS ---")

        for ciudad, vecinos in self.grafo.items():
            for destino, minutos in vecinos:
                # Evitar mostrar cada carretera dos veces.
                if ciudad < destino:
                    print(
                        f"{ciudad} <-> {destino}: "
                        f"{minutos} minutos"
                    )

    def dijkstra(self, origen, destino):
        if origen not in self.grafo:
            raise ValueError("La ciudad de origen no existe.")

        if destino not in self.grafo:
            raise ValueError("La ciudad de destino no existe.")

        distancias = {
            ciudad: float("inf")
            for ciudad in self.grafo
        }

        anteriores = {
            ciudad: None
            for ciudad in self.grafo
        }

        distancias[origen] = 0
        cola = [(0, origen)]

        while cola:
            tiempo_actual, ciudad_actual = heapq.heappop(cola)

            # Ignorar resultados que ya quedaron desactualizados.
            if tiempo_actual > distancias[ciudad_actual]:
                continue

            if ciudad_actual == destino:
                break

            for vecino, minutos in self.grafo[ciudad_actual]:
                nuevo_tiempo = tiempo_actual + minutos

                if nuevo_tiempo < distancias[vecino]:
                    distancias[vecino] = nuevo_tiempo
                    anteriores[vecino] = ciudad_actual

                    heapq.heappush(
                        cola,
                        (nuevo_tiempo, vecino)
                    )

        # No existe un camino entre las ciudades.
        if distancias[destino] == float("inf"):
            return None, float("inf")

        # Reconstruir el camino desde el destino al origen.
        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()

        return camino, distancias[destino]

    def buscar_ruta(self, origen, destino):
        camino, tiempo = self.dijkstra(origen, destino)

        if camino is None:
            print("No existe una ruta entre esas ciudades.")
            return

        print("\n--- RUTA MÁS RÁPIDA ---")
        print("Recorrido:", " -> ".join(camino))
        print("Número de tramos:", len(camino) - 1)
        print("Tiempo total:", tiempo, "minutos")


def main():
    gps = SistemaGPS()

    # Ciudades y carreteras iniciales de ejemplo.
    for ciudad in ["Managua", "Masaya", "Granada", "Leon"]:
        gps.agregar_ciudad(ciudad)

    gps.agregar_ruta("Managua", "Masaya", 35)
    gps.agregar_ruta("Masaya", "Granada", 30)
    gps.agregar_ruta("Managua", "Granada", 80)
    gps.agregar_ruta("Managua", "Leon", 90)

    while True:
        print("\n===== SISTEMA DE NAVEGACIÓN GPS =====")
        print("1. Mostrar ciudades")
        print("2. Agregar ciudad")
        print("3. Agregar ruta")
        print("4. Mostrar rutas")
        print("5. Buscar ruta más rápida")
        print("6. Salir")

        try:
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                gps.mostrar_ciudades()

            elif opcion == "2":
                ciudad = input("Nombre de la ciudad: ")
                gps.agregar_ciudad(ciudad)

            elif opcion == "3":
                origen = input("Ciudad de origen: ")
                destino = input("Ciudad de destino: ")
                minutos = int(input("Tiempo en minutos: "))

                gps.agregar_ruta(origen, destino, minutos)

            elif opcion == "4":
                gps.mostrar_rutas()

            elif opcion == "5":
                origen = input("Ciudad de origen: ").strip()
                destino = input("Ciudad de destino: ").strip()

                gps.buscar_ruta(origen, destino)

            elif opcion == "6":
                print("Gracias por utilizar el sistema GPS.")
                break

            else:
                print("Opción incorrecta. Intente nuevamente.")

        except ValueError as error:
            print("Error:", error)

        except (EOFError, KeyboardInterrupt):
            print("\nPrograma finalizado.")
            break


if __name__ == "__main__":
    main()
