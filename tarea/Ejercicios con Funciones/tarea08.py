"""
Escribir una función que reciba como parámetros: otra función y una lista, y devuelva otra
lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
"""

def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Inicializar un diccionario vacío para almacenar las frecuencias
    frecuencias = {}
    
    # Iterar a través de las palabras y contar su frecuencia
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para considerar palabras iguales sin importar la capitalización
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    
    return frecuencias

# Ejemplo de uso:
texto = "Este es un ejemplo de texto. Este texto contiene palabras, y algunas palabras se repiten más que otras."
resultado = contar_palabras(texto)

# Imprimir el diccionario de frecuencias
for palabra, frecuencia in resultado.items():
    print(f"'{palabra}': {frecuencia}")
