def multiplicacion_rusa(a, b):
    # Caso base
    if b == 0:
        return 0

    # Caso recursivo
    if b > 0:
        return a + multiplicacion_rusa(a, b - 1)

    return -multiplicacion_rusa(a, -b)


print(multiplicacion_rusa(5, 3))