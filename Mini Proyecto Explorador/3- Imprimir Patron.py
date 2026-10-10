def imprimir_patron(n, fila=1):
    # Caso base
    
    if fila > n:
        return
    print("*" * fila)
    
    # Caso recursivo
    imprimir_patron(n, fila + 1)


imprimir_patron(3)