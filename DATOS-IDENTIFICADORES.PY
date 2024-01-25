# Programa para calcular el área de un rectángulo

# Función para calcular el área del rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dado su base y altura.

    :param base: La base del rectángulo.
    :param altura: La altura del rectángulo.
    :return: El área del rectángulo.
    """
    area = base * altura
    return area

# Solicitar al usuario la base y altura del rectángulo
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Calcular el área del rectángulo utilizando la función
area_resultante = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Imprimir el resultado
print(f"El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es: {area_resultante}")

