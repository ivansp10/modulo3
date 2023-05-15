# Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las
# consonantes restantes y su posición dentro de dicha palabra.

# creamos las variables palabra y palabra_
palabra = "paralelepípedo"
palabra_ = ""
# creamos la variable vocales que contiene una lista de vocales
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó",
           "ú"]
# convertimos la variable palabra a minusculas
palabra.lower()

# Recorrimos la variable palabra con un for y que nos entregue la variable palabre sin vocales
for letra in palabra:
    if (letra in vocales):
        continue
    palabra_ += letra
print(palabra_)
# imprimimos la variable palabra_ y usamos la funcion enumerate que nos devuelve la posicion de la letra dentro de la palabra
print(list(enumerate(palabra_)))
