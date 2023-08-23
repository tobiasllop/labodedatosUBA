import csv
nombre_archivo = "arbolado-en-espacios-verdes.csv"

#1
def leer_parque(nombre_archivo, parque):
        lista_arboles = []
        f = open(nombre_archivo)
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
                if fila[10] == parque:
                        diccionario = dict(zip(encabezado, fila))
                        lista_arboles.append(diccionario)
        return lista_arboles

#print(leer_parque(nombre_archivo, "GENERAL PAZ"))
res = 0
for i in leer_parque(nombre_archivo, "GENERAL PAZ"):
        res += 1
print(res)

#2
def especies(lista_arboles):
        res = []