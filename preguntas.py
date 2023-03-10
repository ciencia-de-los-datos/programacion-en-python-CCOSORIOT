"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
#Lectura y limpieza de datos
def Datos():
    Data = open('data.csv', 'r').readlines()
    Data = [z.replace("\n", "") for z in Data]
    Data = [z.split("\t") for z in Data]
    return Data

#Pregunta 1
def pregunta_01():
    Columna2 = [z[1] for z in Datos()[0:]]

    Suma = 0
    for i in Columna2:
        Suma += int(i)
    Suma
    return Suma

#Pregunta 2
def pregunta_02():
    Columna1 = [z[0] for z in Datos()[0:]]

    Grupos = list(set(Columna1))
    Lista_Conteo = []

    for i in Grupos:
        Conteo = Columna1.count(i)
        Lista_Conteo.append(Conteo)
    Lista_Tuplas = sorted(list(zip(Grupos, Lista_Conteo)))
    Lista_Tuplas
    return Lista_Tuplas

#Pregunta 3
def pregunta_03():
    Tabla1 = sorted([z[:2] for z in Datos()])
    Columna1 = [z[0] for z in Datos()[0:]]
    Grupos = sorted(list(set(Columna1)))

    Suma = 0
    ListaSuma = []

    for i in Grupos:
        Suma = 0
        for j in Tabla1:    
            if i[0] == j[0]:
                Suma += int(j[1])
        ListaSuma.append(Suma)
    Lista_Tuplas = sorted(list(zip(Grupos, ListaSuma)))
    Lista_Tuplas
    return Lista_Tuplas

#Pregunta 4
def pregunta_04():
    Columna3 = [z[2] for z in Datos()[0:]]
    Campos_Fechas = [z.split("-") for z in Columna3]
    Columna_Mes = [z[1] for z in Campos_Fechas]

    Grupos = list(set(Columna_Mes))
    Lista_Conteo = []

    for i in Grupos:
        Conteo = Columna_Mes.count(i)
        Lista_Conteo.append(Conteo)
    Lista_Tuplas = sorted(list(zip(Grupos, Lista_Conteo)))
    Lista_Tuplas
    return Lista_Tuplas

#Pregunta 5
def pregunta_05():
    Tabla1 = sorted([z[:2] for z in Datos()])
    Columna1 = [z[0] for z in Datos()[0:]]
    Grupos = sorted(list(set(Columna1)))

    Maximo: int = 0
    ListaMaximo = []
    for i in Grupos:
        Maximo = 0
        for j in Tabla1:
            if i[0] == j[0]:
                if int(j[1]) > Maximo:
                    Maximo = int(j[1])
        ListaMaximo.append(Maximo)

    Columna2 = [z[1] for z in Datos()[0:]]
    Minimo = max(Columna2)
    ListaMinimo = []
    for i in Grupos:
        Minimo = int(max(Columna2))
        for j in Tabla1:
            if i[0] == j[0]:
                if int(j[1]) < Minimo:
                    Minimo = int(j[1])
        ListaMinimo.append(Minimo)

    Lista_Tuplas = sorted(list(zip(Grupos, ListaMaximo, ListaMinimo)))
    Lista_Tuplas
    return Lista_Tuplas

#Pregunta 6
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return

#Pregunta 7
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return

#Pregunta 8
def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return

#Pregunta 9
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return

#Pregunta 10
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return

#Pregunta 11
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return

#Pregunta 12
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
