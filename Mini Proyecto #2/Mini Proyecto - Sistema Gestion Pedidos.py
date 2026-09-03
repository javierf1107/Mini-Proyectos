# SISTEMA DE GESTION DE PEDIDOS
# Herencia + Pila + Validaciones


# CLASE PADRE
class Pedido:

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente

    def mostrar_pedido(self):
        print("Numero de pedido:", self.numero)
        print("Cliente:", self.cliente)


# CLASE HIJA
class PedidoComida(Pedido):

    def __init__(self, numero, cliente, comida):
        super().__init__(numero, cliente)
        self.comida = comida

    def mostrar_pedido(self):
        super().mostrar_pedido()
        print("Tipo: Comida")
        print("Comida:", self.comida)


# CLASE HIJA
class PedidoProducto(Pedido):

    def __init__(self, numero, cliente, producto):
        super().__init__(numero, cliente)
        self.producto = producto

    def mostrar_pedido(self):
        super().mostrar_pedido()
        print("Tipo: Producto")
        print("Producto:", self.producto)


# CREAR LA PILA
pila = []


# MENU PRINCIPAL
while True:

    print("\n===== SISTEMA DE GESTION DE PEDIDOS =====")
    print("1. Llenar pila")
    print("2. Atender pedido")
    print("3. Mostrar pila")
    print("4. Verificar si la pila esta vacia")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")


    # VALIDAR OPCION
    if opcion not in ["1", "2", "3", "4", "5"]:
        print("Error: seleccione una opcion del 1 al 5.")
        continue


    # ==========================================
    # 1. LLENAR PILA
    # ==========================================
    if opcion == "1":

        while True:

            print("\n===== AGREGAR PEDIDO =====")

            # VALIDAR NUMERO
            while True:

                numero = input("Ingrese el numero del pedido: ")

                if numero == "":
                    print("Error: el numero no puede estar vacio.")

                elif not numero.isdigit():
                    print("Error: el numero debe contener solamente numeros.")

                else:
                    break


            # VALIDAR CLIENTE
            while True:

                cliente = input("Ingrese el nombre del cliente: ")

                if cliente == "":
                    print("Error: el cliente no puede estar vacio.")

                elif not cliente.replace(" ", "").isalpha():
                    print("Error: el nombre debe contener solamente letras.")

                else:
                    break


            # SELECCIONAR TIPO
            while True:

                print("\nTipo de pedido:")
                print("1. Comida")
                print("2. Producto")

                tipo = input("Seleccione el tipo: ")

                if tipo == "1" or tipo == "2":
                    break

                else:
                    print("Error: seleccione 1 o 2.")


            # PEDIDO DE COMIDA
            if tipo == "1":

                while True:

                    comida = input("Ingrese la comida: ")

                    if comida == "":
                        print("Error: la comida no puede estar vacia.")

                    else:
                        break

                pedido = PedidoComida(numero, cliente, comida)


        