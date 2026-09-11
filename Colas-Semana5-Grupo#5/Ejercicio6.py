from queue_structure import Queue

cola = Queue()

cola.enqueue("Pedro")
cola.enqueue("Luis")
cola.enqueue("Ana")
cola.enqueue("Carlos")

if cola.is_empty():

    print("La cola esta vacia")

else:

    temporal = Queue()
    encontrado = None

    while not cola.is_empty():

        nombre = cola.dequeue()

        if encontrado is None and nombre.startswith("A"):

            encontrado = nombre

        else:

            temporal.enqueue(nombre)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())

    if encontrado is not None:

        cola.enqueue(encontrado)

    print("Cola con el primer nombre que inicia con A al fondo:")

    temporal = Queue()

    while not cola.is_empty():

        elemento = cola.dequeue()

        print(elemento, end=" ")

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())