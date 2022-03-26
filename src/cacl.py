
def get_fractions(entrada):
    """
    Función que recibe un string y verifica si es una fracción
    o un número y regresa el valor numérico de la fracción en
    caso que sea fracción

    Args:
      entrada: un string o un float

    Returns:
        numero -> el valor de la fracción o el valor del número en float

    """
    numero = 0
    try:
        if(isinstance(entrada, str)):
            print(entrada)
            if "/" in entrada:
                arr = entrada.split("/")
                numerador = arr[0]
                denominador = arr[1]
                # print(arr)
                numero = float(numerador) / float(denominador)
                # print(arr, numero)
            else:
                numero = float(entrada)
                print(type(numero))

        if(isinstance(entrada, int) or isinstance(entrada, float)):
            numero = entrada
    except ValueError:
        print("Error de formato de numero")

    return numero


def suma(a, b):
    """
    Función que suma dos números, pueden ser enteros,
    flotantes o fracciones

    Args:
      a: sumando 1
      b: sumando 2

    Returns:
        suma de ambos números (a+b)

    """
    sumando_a = get_fractions(a)
    sumando_b = get_fractions(b)
    return sumando_a + sumando_b


def multiplicacion(a, b):
    """
    Función que multiplica dos números, pueden ser enteros,
    flotantes o fracciones

    Args:
      a: número 1 que se va a multiplicar
      b: número 2 que se va a multiplicar

    Returns:
        multiplicación de a * b

    """
    mult_a = get_fractions(a)
    mult_b = get_fractions(b)
    return mult_a * mult_b