"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    counter = dict()
    with open('./files/input/data.csv', 'r') as file:
        for line in file.readlines():
            letter = line.split('\t')[0]
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1

    result = sorted(counter.items(), key=lambda x: x[0])
    
    return result
