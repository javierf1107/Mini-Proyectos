cola_pedidos = []

def agregar_pedido():
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))

    pedido = {
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad
    }

    cola_pedidos.append(pedido)

    print("Pedido agregado correctamente.")


def procesar_pedido():
    if not cola_pedidos:
        print("No hay pedidos pendientes.")
        return

    pedido = cola_pedidos.pop(0)

    print("\nPedido procesado:")
    print("Cliente:", pedido["cliente"])
    print("Producto:", pedido["producto"])
    print("Cantidad:", pedido["cantidad"])


def ver_siguiente():
    if not cola_pedidos:
        print("No hay pedidos pendientes.")
        return

    pedido = cola_pedidos[0]

    print("\nSiguiente pedido:")
    print("Cliente:", pedido["cliente"])
    print("Producto:", pedido["producto"])
    print("Cantidad:", pedido["cantidad"])


def mostrar_cola():
    if not cola_pedidos:
        print("La cola está vacía.")
        return

    print("\n--- PEDIDOS PENDIENTES ---")

    for posicion, pedido in enumerate(cola_pedidos, 1):
        print(
            posicion,
            "- Cliente:", pedido["cliente"],
            "| Producto:", pedido["producto"],
            "| Cantidad:", pedido["cantidad"]
        )


def menu():
    while True:

        print("\n==============================")
        print("       SMARTBUSINESS")
        print("==============================")
        print("1. Agregar pedido")
        print("2. Procesar pedido")
        print("3. Ver siguiente pedido")
        print("4. Mostrar cola")
        print("5. Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pedido()

        elif opcion == "2":
            procesar_pedido()

        elif opcion == "3":
            ver_siguiente()

        elif opcion == "4":
            mostrar_cola()

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()
