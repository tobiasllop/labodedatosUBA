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
        res = set()
        for arbol in lista_arboles:
                res.add(arbol["nombre_com"])
        return res
#print(especies(leer_parque(nombre_archivo, "GENERAL PAZ")))

#3
def contar_ejemplares(lista_arboles):
        res = {}
        for arbol in lista_arboles:
                if arbol["nombre_com"] in res:
                        res[arbol["nombre_com"]] += 1
                else:
                      res[arbol["nombre_com"]] = 1
        return res

print(contar_ejemplares(leer_parque(nombre_archivo, "GENERAL PAZ"))["Jacarandá"])

#5
def obtener_inclinaciones(lista_arboles, especie):
    res = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            res.append(arbol["inclinacio"])
    return res

print(obtener_inclinaciones(leer_parque(nombre_archivo, "GENERAL PAZ"), "Jacarandá"))
