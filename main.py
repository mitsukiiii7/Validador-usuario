from validaciones import validar_no_vacio, validar_longitud, validar_primer_caracter, validar_caracteres_permitidos
from clasificacion import clasificar_caracteres, determinar_nivel
from estadisticas import calcular_porcentajes, calcular_repetidos_consecutivos, comparar_mitades
from transformaciones import espejar, ordenar_burbuja

def validar_usuario(nombre: str) -> bool:

    if not validar_no_vacio(nombre):
        return False
    if not validar_longitud(nombre):
        return False
    if not validar_primer_caracter(nombre):
        return False
    if not validar_caracteres_permitidos(nombre):
        return False

    resultado = clasificar_caracteres(nombre)
    if resultado[0] is None:  
        return False
    (tiene_letra, tiene_numero, tiene_simbolo,
     cant_letras, cant_numeros, cant_simbolos) = resultado
    
    longitud = len(nombre)

    porc_letras, porc_numeros, porc_simbolos = calcular_porcentajes(cant_letras, cant_numeros, cant_simbolos, longitud)
    repetidos = calcular_repetidos_consecutivos(nombre)
    mitades_iguales = comparar_mitades(nombre)

    print("Longitud total: " + str(longitud))
    print("Porcentaje de letras: " + str(porc_letras) + "%")
    print("Porcentaje de números: " + str(porc_numeros) + "%")
    print("Porcentaje de símbolos: " + str(porc_simbolos) + "%")
    print("Caracteres repetidos consecutivos: " + str(repetidos))
    print("Primera mitad igual a segunda mitad: " + str(mitades_iguales))

    ultimo_ascii = ord(nombre[-1])
    termina_en_simbolo = (ultimo_ascii == 95 or ultimo_ascii == 46)

    nombre_espejado = espejar(nombre)
    nombre_ordenado = ordenar_burbuja(nombre)

    nivel = determinar_nivel(tiene_letra, tiene_numero, tiene_simbolo,
                             cant_numeros, cant_simbolos, longitud, termina_en_simbolo)

    if nivel == "Básico":
        print("Nombre de usuario nivel: Básico")
    elif nivel == "Intermedio":
        print("Nombre de usuario nivel: Intermedio")
    elif nivel == "Avanzado":
        print("Nombre de usuario nivel: Avanzado")
    else:
        print("El nombre de usuario no cumple completamente las condiciones de: Básico, Intermedio ni Avanzado: Sin categoría")

    print("Nombre espejado: " + nombre_espejado)
    print("Nombre ordenado: " + nombre_ordenado)

    return nivel != "Sin categoría"

if __name__ == "__main__":
    usuario = input("Ingrese nombre de usuario: ")
    validar_usuario(usuario)
