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

    menor = cola.front()

    while not cola.is_empty():

        elemento = cola.dequeue()

        if elemento < menor:
            menor = elemento

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        elemento = temporal.dequeue()

        if elemento != menor:
            cola.enqueue(elemento)

    nueva_cola = Queue()

    nueva_cola.enqueue(menor)

    while not cola.is_empty():

        nueva_cola.enqueue(cola.dequeue())

    cola = nueva_cola

    print("El numero menor fue colocado al frente.")

    temporal = Queue()

    while not cola.is_empty():

        elemento = cola.dequeue()

        print(elemento, end=" ")

        temporal.enqueue(elemento)

    while not temporal.is_empty():

        cola.enqueue(temporal.dequeue())