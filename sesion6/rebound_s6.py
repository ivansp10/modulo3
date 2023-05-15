# Escribir un programa que analice un número, e indique si es positivo o negativo, y si es par o impar.
# En caso de ser cero, también indicarlo. Se debe usar la expresión if-elif-else, y no usar
# subcondiciones; en su lugar, usar condiciones anidadas.


num = int(input("Inserte un número: "))

if (num % 2 == 0 and num > 0):
    print("El número ingresado es un número par positivo")
elif (num % 2 == 0 and num < 0):
    print("El número ingresado es un número par negativo")
elif (num % 2 != 0 and num < 0):
    print("El número ingresado es un número impar negativo")
elif (num % 2 != 0 and num > 0):
    print("El número ingresado es un número impar positivo")
else:
    print("El número ingresado es 0")
