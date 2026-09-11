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

    nueva_cola = Queue()

    if encontrado is not None:

        nueva_cola.enqueue(encontrado)

    while not temporal.is_empty():

        nueva_cola.enqueue(temporal.dequeue())

    cola = nueva_cola

    print("Cola con el primer nombre que inicia con A al frente:")

    temporal = Queue()

    while not cola.is_empty():

        elemento = cola.dequeue()

        print(elemento, end=" ")

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())