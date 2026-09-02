#Ejercicio 1

# Pila de números
pila = []

# 1. Función para validar números enteros
def pedir_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un número entero.")


# 2. Agregar números
def agregar_numero():
    numero = pedir_entero("Ingrese un número entero: ")
    pila.append(numero)
    print("Número agregado correctamente.")


# 3. Contar elementos
def contar_elementos():
    cantidad = len(pila)
    print(f"La pila tiene {cantidad} elementos.")


# 4. Mostrar todos los elementos
def mostrar_elementos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elementos de la pila:")

        for numero in pila:
            print(numero)


# 5. Promedio de todos los números
def promedio_numeros():
    if len(pila) == 0:
        print("No se puede calcular el promedio porque la pila está vacía.")
    else:
        suma = 0

        for numero in pila:
            suma = suma + numero

        promedio = suma / len(pila)

        print(f"El promedio es: {promedio}")


# Menú principal
while True:

    print("\n***** MENÚ DE OPCIONES *****")
    print("1. Agregar números")
    print("2. Contar elementos")
    print("3. Mostrar todos los elementos")
    print("4. Promedio de todos los números")
    print("5. Salir del sistema")

    opcion = pedir_entero("Seleccione una opción: ")

    if opcion == 1:
        agregar_numero()

    elif opcion == 2:
        contar_elementos()

    elif opcion == 3:
        mostrar_elementos()

    elif opcion == 4:
        promedio_numeros()

    elif opcion == 5:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Seleccione del 1 al 5.")