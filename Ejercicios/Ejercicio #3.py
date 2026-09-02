#Ejercicio #3

# Programa para trabajar con una pila de departamentos de Nicaragua


# Declaramos la pila
pila = []


# 1. Agregar un departamento a la pila
def agregar_departamento():
    departamento = input("Ingrese el nombre del departamento: ")
    pila.append(departamento)
    print("Departamento agregado correctamente.")


# 2. Remover un departamento de la pila
def remover_departamento():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        departamento = pila.pop()
        print("Departamento removido:", departamento)


# 3. Imprimir todos los departamentos de la pila
def imprimir_departamentos():
    if len(pila) == 0:
        print("La pila está vacía.")
    else:
        print("\nDepartamentos de la pila:")

        for departamento in reversed(pila):
            print(departamento)


# 4. Mostrar el menú
def menu():
    while True:

        print("\n***** MENÚ DE OPCIONES *****")
        print("1. Agregar departamento")
        print("2. Remover departamento")
        print("3. Imprimir departamentos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_departamento()

        elif opcion == "2":
            remover_departamento()

        elif opcion == "3":
            imprimir_departamentos()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


# Ejecutamos el menú
menu()