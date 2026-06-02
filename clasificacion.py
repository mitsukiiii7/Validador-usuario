def clasificar_caracteres(nombre: str):

    tiene_letra = False
    tiene_numero = False
    tiene_simbolo = False
    cant_letras = 0
    cant_numeros = 0
    cant_simbolos = 0

    for i in range(len(nombre)):
        num_ascii = ord(nombre[i])

        if num_ascii == 32:
            print("No puede contener espacios.")
            return (None, None, None, None, None, None)

        es_letra = (65 <= num_ascii <= 90) or (97 <= num_ascii <= 122) or num_ascii == 209 or num_ascii == 241
        es_numero = (48 <= num_ascii <= 57)
        es_simbolo = (num_ascii == 95 or num_ascii == 46)

        if es_letra:
            tiene_letra = True
            cant_letras += 1
        elif es_numero:
            tiene_numero = True
            cant_numeros += 1
        elif es_simbolo:
            tiene_simbolo = True
            cant_simbolos += 1
        else:

            print("Carácter no permitido.")
            return (None, None, None, None, None, None)

    return (tiene_letra, tiene_numero, tiene_simbolo, cant_letras, cant_numeros, cant_simbolos)

def determinar_nivel(tiene_letra: bool, tiene_numero: bool, tiene_simbolo: bool,
                     cant_numeros: int, cant_simbolos: int, longitud: int,
                     termina_en_simbolo: bool) -> str:
                         
    if cant_numeros == 0 and cant_simbolos == 0 and 6 <= longitud <= 8:
        return "Básico"

    if tiene_letra and tiene_numero and not tiene_simbolo and longitud >= 8:
        return "Intermedio"

    if tiene_letra and tiene_numero and tiene_simbolo and longitud >= 12 and not termina_en_simbolo:
        return "Avanzado"
    return "Sin categoría"
