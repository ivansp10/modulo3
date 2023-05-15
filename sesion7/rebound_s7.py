# Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, e imprimir en
# pantalla el valor de cada elemento indicando si es par, impar o cero.


# creamos la lista de numeros enteros
lista = [-3, -2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# recorrimos la lista y aplicamos condicionales para determinar si es par,impar o cero
for num in lista:

    if (num == 0):
        print(f"El número es {num}")
    elif (num % 2 == 0):
        print(f"El número {num} es un número par")
    elif (num % 2 != 0):
        print(f"El número {num} es un número impar")
