# Estructura de datos: Cola (Queue)

class Queue:

    def __init__(self):
        self.items = []

    # Agregar un elemento al fondo
    def enqueue(self, elemento):
        self.items.append(elemento)

    # Eliminar el elemento del frente
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    # Consultar el elemento del frente
    def front(self):
        if not self.is_empty():
            return self.items[0]

    # Verificar si la cola esta vacia
    def is_empty(self):
        return len(self.items) == 0

    # Obtener la cantidad de elementos
    def size(self):
        return len(self.items)