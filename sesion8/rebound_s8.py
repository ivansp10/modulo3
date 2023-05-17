# En esta actividad trabajaremos con listas. Tomando la lista que se entrega a continuación, se
# solicita realizar las siguientes acciones en el orden indicado:
# 1. Eliminar los elementos duplicados.
# 2. Ordenar la lista resultante en orden ascendente.

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

# transformamos la lista a un set para eliminar elementos repetidos
mi_lista_1 = list(set(mi_lista))

# ordenamos la lista de forma ascendente con el metodo sort
mi_lista_1.sort()
print(sorted(mi_lista_1))
