from queue_structure import Queue

cola = Queue()

cola.enqueue(4)
cola.enqueue(9)
cola.enqueue(16)
cola.enqueue(25)

if cola.is_empty():

    print("La cola esta vacia")

else:

    temporal = Queue()
    raices = Queue()

    while not cola.is_empty():

        numero = cola.dequeue()

        raiz = numero ** 0.5

        raices.enqueue(raiz)
        temporal.enqueue(numero)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())

    print("Cola original:")

    temporal = Queue()

    while not cola.is_empty():

        elemento = cola.dequeue()

        print(elemento, end=" ")

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())

    print()

    print("Cola temporal con las raices:")

    while not raices.is_empty():

        print(raices.dequeue(), end=" ")