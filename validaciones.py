def validar_usuario(nombre):
    if nombre == "":
        print("El usuario debe contener caracteres")
        return False

    if len(nombre) < 6 or len(nombre) > 15:
        return False

    primer_ascii = ord(nombre[0])
    if primer_ascii >= 48 and primer_ascii <= 57:
        print("No puede comenzar con un número.")
        return False

    tiene_letra = False
    tiene_numero = False
    tiene_simbolo = False

    cant_letras = 0
    cant_numeros = 0
    cant_simbolos = 0

    for i in range(len(nombre)):
        c = nombre[i]
        num_ascii = ord(c)

        if num_ascii == 32:
            print("No puede contener espacios.")
            return False

        es_letra = (num_ascii >= 65 and num_ascii <= 90) or (num_ascii >= 97 and num_ascii <= 122) or num_ascii == 209 or num_ascii == 241
        es_numero = (num_ascii >= 48 and num_ascii <= 57)
        es_simbolo = (num_ascii == 95 or num_ascii == 46)

        # Esto ahora está dentro del for (indentado correctamente)
        if es_letra:
            tiene_letra = True
            cant_letras = cant_letras + 1
        elif es_numero:
            tiene_numero = True
            cant_numeros = cant_numeros + 1
        elif es_simbolo:
            tiene_simbolo = True
            cant_simbolos = cant_simbolos + 1
        else:
            print("Carácter no permitido.")
            return False

    # Ahora USA las variables para que no estén "oscuras"
    if not tiene_letra:
        print("Debe contener al menos una letra.")
        return False

    # Por ejemplo, mostrar que también se detectaron números y símbolos
    if tiene_numero:
        print("El nombre contiene números.")
    if tiene_simbolo:
        print("El nombre contiene símbolos.")

    # Si quieres, puedes usarlos para decidir una categoría más adelante
    return True