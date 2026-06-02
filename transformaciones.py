def espejar(texto: str) -> str:
    
    invertido = ""
    i = len(texto) - 1
    while i >= 0:
        invertido += texto[i]
        i -= 1
    return invertido

def ordenar_burbuja(texto: str) -> str:
    
    n = len(texto)
    caracteres = [None] * n
    for k in range(n):
        caracteres[k] = texto[k]
        
    for i in range(n):
        for j in range(n - i - 1):
            if ord(caracteres[j]) > ord(caracteres[j+1]):
                temp = caracteres[j]
                caracteres[j] = caracteres[j+1]
                caracteres[j+1] = temp
                
    resultado = ""
    for k in range(n):
        resultado += caracteres[k]
    return resultado
