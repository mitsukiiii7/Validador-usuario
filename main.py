"""Función principal que integra todos los módulos."""

from validaciones import validar_no_vacio, validar_longitud, validar_primer_caracter, validar_caracteres_permitidos
from clasificacion import clasificar_caracteres, determinar_nivel
from estadisticas import calcular_porcentajes, calcular_repetidos_consecutivos, comparar_mitades
from transformaciones import espejar, ordenar_burbuja

def validar_usuario(nombre: str) -> bool:
    """Valida el nombre de usuario, muestra estadísticas y clasifica el nivel."""
    # Validaciones iniciales
    if not validar_no_vacio(nombre):
        return False
    if not validar_longitud(nombre):
        return False
    if not validar_primer_caracter(nombre):
        return False
    if not validar_caracteres_permitidos(nombre):
        return False

    # Clasificación de caracteres
    resultado = clasificar_caracteres(nombre)
    if resultado[0] is None:  # hubo error (carácter no permitido)
        return False
    (tiene_letra, tiene_numero, tiene_simbolo,
     cant_letras, cant_numeros, cant_simbolos) = resultado
    
    longitud = len(nombre)

    # Estadísticas
    porc_letras, porc_numeros, porc_simbolos = calcular_porcentajes(cant_letras, cant_numeros, cant_simbolos, longitud)
    repetidos = calcular_repetidos_consecutivos(nombre)
    mitades_iguales = comparar_mitades(nombre)

    # Mostrar resultados (sin f-strings)
    print("Longitud total: " + str(longitud))
    print("Porcentaje de letras: " + str(porc_letras) + "%")
    print("Porcentaje de números: " + str(porc_numeros) + "%")
    print("Porcentaje de símbolos: " + str(porc_simbolos) + "%")
    print("Caracteres repetidos consecutivos: " + str(repetidos))
    print("Primera mitad igual a segunda mitad: " + str(mitades_iguales))

    # Datos para nivel
    ultimo_ascii = ord(nombre[-1])
    termina_en_simbolo = (ultimo_ascii == 95 or ultimo_ascii == 46)

    # Transformaciones
    nombre_espejado = espejar(nombre)
    nombre_ordenado = ordenar_burbuja(nombre)

    # Clasificación del nivel
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

# Ejemplo de uso (opcional)
if __name__ == "__main__":
    usuario = input("Ingrese nombre de usuario: ")
    validar_usuario(usuario)