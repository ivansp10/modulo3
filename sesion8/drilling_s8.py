# Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
# • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
# • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
# • Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
# segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
# • Finalmente, imprimiremos en pantalla el diccionario resultante.


lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

claves = ['A', 'B', 'C', 'D']

diccionario = {}
lista_1 = []

for i, sublista in enumerate(lista):
    if sublista[0] == 0:
        continue  # Omitir la sublista completa si el primer elemento es cero

    elementos_sublista = []
    for elemento in sublista:
        if elemento == 0:
            continue  # Omitir la impresión del cero

        elementos_sublista.append(elemento)
    lista_1.append(elementos_sublista)

print(lista_1)
for i in range(len(lista_1)):
    # le otorgamos las clases al diccionario
    diccionario[claves[i]] = lista_1[i]
print(diccionario)
