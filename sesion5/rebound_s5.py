# Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla.
# Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay
# entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.

n = int(input("Ingrese un numero: "))
fac = 1

if (n > 0):
    for num in range(1, n+1):
        fac *= num

    print(fac)
else:
    fac = 1
    print(fac)
