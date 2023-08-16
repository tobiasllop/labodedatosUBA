import random
import csv

"""
altura = 100
i = 1
while i <= 10:
# Calcula la nueva altura
    altura = 3/5*altura
    # Muestra en pantalla los nuevos datos
    print(i, end = ' ')
    print(round(altura,3))
    # Actualiza el contador de rebotes
    i+=1
    
def suma_gauss(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

print(suma_gauss(5))
"""

def maximo(a,b):
    if a >= b:
        res = a
    else:
        res = b
    return res

#print(maximo(2,3))

def tachar_pares(lista):
    res = []
    for i in lista:
        if i%2 == 0:
            res.append("x")
        else:
            res.append(i)
    return res

#print(tachar_pares([4,7,9,2]))

lista = ["banana", "manzana", "mandarina"]

def geringoso(palabra):
    res = ""
    for i in palabra:
        res += i
        if i == "o":
            res += "po"
        elif i == "a":
            res += "pa"
        elif i == "e":
            res += "pe"
        elif i == "i":
            res += "pi"
        elif i == "u":
            res += "pu"
    return res
    
def traductor_geringoso(lista):
    res = {}
    lista_geringosa = []
    for i in lista:
        lista_geringosa.append(geringoso(i))
    res = dict(zip(lista, lista_geringosa))
    return res
    
#print(traductor_geringoso(lista))
    
def generala_tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

#print(generala_tirar())
nombre_archivo = "/home/clinux01/Documentos/Labo-datos/clase 1/datame.txt"
f = open(nombre_archivo, "rt")
data = f.read()
f.close()
#data
#print(data)

"""
with open(nombre_archivo, 'rt') as f:
    for l in f:
        if "estudiantes" in l:
            print(l)
"""

nombre_archivo = "/home/clinux01/Documentos/Labo-datos/clase 1/cronograma_sugerido.csv"
asignaturas = []
cuatrimestre = []
with open(nombre_archivo, 'rt') as f:
    for l in f:
        columnas = l.split(",")
        asignaturas.append(columnas[1])
        cuatrimestre.append(columnas[0])
asignaturas.remove("Asignatura")
#print(asignaturas)

cuatrimestre.remove("Cuatrimestre")
def cuantas_materias(n):
    contador = 0
    for i in cuatrimestre:
        if int(i) == n:
            contador += 1
    return contador
#print(cuantas_materias(5))

def registros(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(zip(encabezado,fila)) # Arma el diccionario de cada fila
            lista.append(registro) # Agrega el diccionario a la lista
    return lista


def materias_cuatrimestre(nombre_archivo, n):
    result = []
    datos = registros(nombre_archivo)
    for d in datos:
        if int(d["Cuatrimestre"]) == n:
            result.append(d)
    return result

print(materias_cuatrimestre(nombre_archivo, 5))

