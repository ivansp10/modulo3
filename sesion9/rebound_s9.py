# Crear una función que acepte 3 números como parámetros, sume todos los valores, y
# adicionalmente reste el segundo y tercer parámetro al primero.
# Al invocar la función, debemos pasarle los parámetros en forma de lista. Esta devolverá ambos
# resultados en una tupla. Los resultados se deben imprimir en pantalla.


numeros = [50, 4, 2]


def operacion(numeros):
    resultado = numeros[0]+numeros[1]+numeros[2]
    resultado_2 = numeros[0]-numeros[1]-numeros[2]
    return resultado, resultado_2


resultado = operacion(numeros)
print(resultado)
