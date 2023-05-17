# Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
# números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
# números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
# multiplicación y división.
# Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
# Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
# creada anteriormente.

# creacion de las funciones de operaciones numericas
def suma(a, b):
    resultado = a+b
    return (resultado)


def resta(a, b):
    resultado = a-b
    return (resultado)


def multiplicacion(a, b):
    resultado = a*b
    return (resultado)


def division(a, b):
    resultado = a/b
    return (resultado)


def operaciones(a, b):
    r_suma = suma(a, b)
    r_resta = resta(a, b)
    r_mult = multiplicacion(a, b)
    r_div = division(a, b)
    return (r_suma, r_resta, r_mult, r_div)


resultado = operaciones(10, 15)
print(resultado)

diccionario = {}
claves = ['Suma', 'Resta', 'Multiplicacion', 'Division']

# asignar los resultados a un diccionario
for i in range(len(resultado)):
    diccionario[claves[i]] = resultado[i]
print(diccionario)
