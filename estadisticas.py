def calcular_porcentajes(cant_letras: int, cant_numeros: int, cant_simbolos: int, longitud: int):

    if longitud == 0:
        return (0, 0, 0)
    porc_letras = (cant_letras * 100) // longitud
    porc_numeros = (cant_numeros * 100) // longitud
    porc_simbolos = (cant_simbolos * 100) // longitud
    return (porc_letras, porc_numeros, porc_simbolos)

def calcular_repetidos_consecutivos(nombre: str) -> int:
    
    repetidos = 0
    for i in range(1, len(nombre)):
        if nombre[i] == nombre[i-1]:
            repetidos += 1
    return repetidos

def comparar_mitades(nombre: str) -> bool:
    
    longitud = len(nombre)
    mitad = longitud // 2
    es_impar = (longitud % 2 == 1)
    for i in range(mitad):
        if es_impar:
            j = i + mitad + 1
        else:
            j = i + mitad
        if nombre[i] != nombre[j]:
            return False
    return True
