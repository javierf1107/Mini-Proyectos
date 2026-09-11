from queue_structure import Queue

cola = Queue()

cola.enqueue("Ana")
cola.enqueue("Pedro")
cola.enqueue("Luis")

if cola.is_empty():

    print("La cola esta vacia")

else:

    primer_elemento = cola.front()

    print("Primer elemento de la cola:", primer_elemento)

    print("La cola sigue igual porque front() no elimina el elemento.")