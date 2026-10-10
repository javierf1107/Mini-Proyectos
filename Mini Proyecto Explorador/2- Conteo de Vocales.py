def contar_vocales(texto):
    # Caso base
    if texto == "":
        return 0

    primera = texto[0].lower()

    if primera in "aeiou":
        cantidad = 1
    else:
        cantidad = 0

    # Caso recursivo
    return cantidad + contar_vocales(texto[1:])


print(contar_vocales("Jude and Jobe"))