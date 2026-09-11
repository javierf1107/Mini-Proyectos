from queue_structure import Queue

cola = Queue()

cola.enqueue("Ana")
cola.enqueue("Pedro")
cola.enqueue("Luis")

if cola.is_empty():

    print("La cola esta vacia")

else:

    print("Cantidad de elementos:", cola.size())