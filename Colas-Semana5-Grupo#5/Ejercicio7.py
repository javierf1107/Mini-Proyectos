from queue_structure import Queue

cola = Queue()

cola.enqueue("Ana")
cola.enqueue("Pedro")
cola.enqueue("Luis")
cola.enqueue("Carlos")

if cola.is_empty():

    print("La cola esta vacia")

else:

    temporal = Queue()

    while not cola.is_empty():

        temporal.enqueue(cola.dequeue())

    pila = []

    while not temporal.is_empty():

        pila.append(temporal.dequeue())

    invertida = Queue()

    while len(pila) > 0:

        invertida.enqueue(pila.pop())

    print("Cola invertida:")

    temporal = Queue()

    while not invertida.is_empty():

        elemento = invertida.dequeue()

        print(elemento, end=" ")

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        invertida.enqueue(temporal.dequeue())