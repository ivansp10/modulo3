### Desarrollo###

nombres = ['Harry Houdini', 'Newton', 'David Blaine',
           'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

### listas vacias para filtrar y agregar nombre##
magos = []
cientificos = []
otros = []

## filtar nombres a traves de un for##
for nombre in nombres:
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)

    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)

    else:
        otros.append(nombre)


## funcion hacer_grandioso##

def hacer_grandioso(lista):
    for i in range(len(lista)):
        lista[i] = 'El gran ' + lista[i]


hacer_grandioso(magos)  # tranformar magos a magos grandiosos


## Funcion imprimir_nombre##
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


## imprimir en pantalla las listas solicitadas##
imprimir_nombres(nombres)
print('***************************************************')
imprimir_nombres(cientificos)
print('***************************************************')
imprimir_nombres(otros)
print('***************************************************')
imprimir_nombres(magos)
