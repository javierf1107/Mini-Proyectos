from queue_structure import Queue

cola = Queue()

cola.enqueue(5)
cola.enqueue(0)
cola.enqueue(8)
cola.enqueue(0)
cola.enqueue(3)
cola.enqueue(0)
cola.enqueue(7)

if cola.is_empty():

    print("La cola esta vacia")

else:

    temporal = Queue()
    ceros = Queue()

    while not cola.is_empty():

        elemento = cola.dequeue()

        temporal.enqueue(elemento)

        if elemento == 0:

            ceros.enqueue(elemento)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())

    print("Elementos ceros:")

    while not ceros.is_empty():

        print(ceros.dequeue(), end=" ")

    print()

    print("La cola original se mantiene igual.")

    temporal = Queue()

    while not cola.is_empty():

        elemento = cola.dequeue()

        print(elemento, end=" ")

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())