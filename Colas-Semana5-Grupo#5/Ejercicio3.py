from queue_structure import Queue

cola = Queue()

cola.enqueue(10)
cola.enqueue(5)
cola.enqueue(20)
cola.enqueue(8)

if cola.is_empty():

    print("La cola esta vacia")

else:

    temporal = Queue()

    mayor = cola.front()

    while not cola.is_empty():

        elemento = cola.dequeue()

        if elemento > mayor:
            mayor = elemento

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        elemento = temporal.dequeue()

        if elemento != mayor:
            cola.enqueue(elemento)

    cola.enqueue(mayor)

    print("El numero mayor fue colocado en el fondo.")

    temporal = Queue()

    while not cola.is_empty():

        elemento = cola.dequeue()

        print(elemento, end=" ")

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())