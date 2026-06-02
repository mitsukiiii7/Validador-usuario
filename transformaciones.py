"""Funciones que transforman el string: espejado y ordenamiento burbuja."""

def espejar(texto: str) -> str:
    """Devuelve el texto invertido carácter por carácter (sin slicing)."""
    invertido = ""
    i = len(texto) - 1
    while i >= 0:
        invertido += texto[i]
        i -= 1
    return invertido

def ordenar_burbuja(texto: str) -> str:
    """Ordena los caracteres según su código ASCII usando Bubble Sort manual."""
    n = len(texto)
    # Crear lista mutable sin usar métodos de lista (excepto asignación por índice)
    caracteres = [None] * n
    for k in range(n):
        caracteres[k] = texto[k]

    # Bubble sort
    for i in range(n):
        for j in range(n - i - 1):
            if ord(caracteres[j]) > ord(caracteres[j+1]):
                temp = caracteres[j]
                caracteres[j] = caracteres[j+1]
                caracteres[j+1] = temp

    # Construir string resultado sin join
    resultado = ""
    for k in range(n):
        resultado += caracteres[k]
    return resultado
