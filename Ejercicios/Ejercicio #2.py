#Ejercicio #2

# Programa para trabajar con una Pila de nombres

# Declaramos la pila
pila = []


# 1. Agregar un nombre a la pila
def agregar_nombre():
    nombre = input("Ingrese el primer nombre: ")
    pila.append(nombre)
    print("Nombre agregado correctamente.")


# 2. Eliminar un nombre de la pila
def eliminar_nombre():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        nombre = pila.pop()
        print("Nombre eliminado:", nombre)


# 3. Mostrar el último elemento en la cima
def mostrar_cima():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("El elemento en la cima es:", pila[-1])


# 4. Buscar un elemento en la pila
def buscar_elemento():
    nombre = input("Ingrese el nombre que desea buscar: ")

    if nombre in pila:
        print("El nombre sí se encuentra en la pila.")
    else:
        print("El nombre no se encuentra en la pila.")


# 5. Contar cuántos elementos tiene la pila
def contar_elementos():
    cantidad = len(pila)
    print("La pila tiene", cantidad, "elementos.")


# 6. Mostrar todos los elementos de la pila
def mostrar_elementos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("Elementos de la pila:")

        for nombre in reversed(pila):
            print(nombre)


# 7. Limpiar la pila
def limpiar_pila():
    pila.clear()
    print("La pila ha sido limpiada.")


# 8. Menú principal
def menu():
    while True:

        print("\n***** MENÚ DE OPCIONES *****")
        print("1. Agregar un nombre a la Pila")
        print("2. Eliminar un nombre de la Pila")
        print("3. Mostrar el último elemento en la Cima")
        print("4. Buscar un elemento en la Pila")
        print("5. Contar cuántos elementos tiene la Pila")
        print("6. Mostrar todos los elementos de la Pila")
        print("7. Limpiar la Pila")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_nombre()

        elif opcion == "2":
            eliminar_nombre()

        elif opcion == "3":
            mostrar_cima()

        elif opcion == "4":
            buscar_elemento()

        elif opcion == "5":
            contar_elementos()

        elif opcion == "6":
            mostrar_elementos()

        elif opcion == "7":
            limpiar_pila()

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


# Ejecutamos el menú
menu()


