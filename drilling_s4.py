"""Requerimos crear un registro de datos personales de tres personas. Los datos que se necesitan
son: su nombre, apellido y teléfono. Para ello, generaremos un diccionario para cada una de las
personas con los datos mencionados, y luego los almacenaremos dentro de una lista. Finalmente,
imprimiremos en pantalla la lista."""

# cremos diccionarios de 3 personas

persona_1 = {"Nombre": "Juan", "Apellido": "Perez", "Teléfono": "12345678"}
persona_2 = {"Nombre": "Héctor", "Apellido": "Tapia", "Teléfono": "98765432"}
persona_3 = {"Nombre": "Martín", "Apellido": "Silva", "Teléfono": "98855522"}


# Almacenamos los diccionarios en una lista
lista = [persona_1, persona_2, persona_3]

# Imprimimos la lista
print(lista)
