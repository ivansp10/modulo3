# Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
# orden de mayor a menor.


# 1- creamos las variables para ingresar los 3 numeros
num_1 = int(input("Ingrese primer número: "))
num_2 = int(input("Ingrese segundo número: "))
num_3 = int(input("Ingrese tercer número: "))

# 2- imponemos la condicion que los numeros deben ser diferentes
# 3- Luego escribimos todas las condiciones para evaluar que numero es mayor y menor

if num_1 != num_2 != num_3:
    if num_1 > num_2 > num_3:
        print(f"{num_1}>{num_2}>{num_3} ")
    elif num_1 > num_3 > num_2:
        print(f"{num_1}>{num_3}>{num_2} ")
    elif num_2 > num_1 > num_3:
        print(f"{num_2}>{num_1}>{num_3} ")
    elif num_2 > num_3 > num_1:
        print(f"{num_2}>{num_3}>{num_1} ")
    elif num_3 > num_2 > num_1:
        print(f"{num_3}>{num_2}>{num_1} ")
    elif num_3 > num_1 > num_2:
        print(f"{num_3}>{num_1}>{num_2} ")
else:
    print("Los números ingresados deben ser diferentes")
