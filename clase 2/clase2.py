#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:45:05 2023

@author: clinux01
"""

import numpy as np
import pandas as pd 
import os


a = np.array([1,2,3,4,5,6])
b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(a[0])
print(b[0])
print(b[0][1])
print([b[0,1]])

c = np.zeros((2,3))
d = np.ones((2))
e = np.arange(2,9,2)
f = np.linspace(0,10, num=5)

impares1 = np.arange(1,20,2)
impares2 = np.linspace(1,19, num=10)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.concatenate((a,b))

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

s = np.concatenate((x,y), axis=0)
t = np.concatenate((x,y), axis=1)

array_ejemplo = np.array([
                            [[0,1,2,3], [4,5,6,7]],
                            [[3,8,10,-1], [0,1,1,0]],
                            [[3,3,3,3], [5,5,5,5]]
                        ])

array_ejemplo.ndim
array_ejemplo.shape[1]
array_ejemplo.size

nueva = array_ejemplo.reshape((12,2))

a = np.array([1,2,3])
b = np.ones(2)
print(a.sum())

data = np.array([[1,2],[3,4],[5,6]])
print(data[0,1])
print(data[1:3])
print(data[1:3,0])


def pisar_elemento(M,e):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i][j] == e:
                M[i][j] = -1
    return M

M = np.array([[0,1,2,3],[4,5,6,7]])

M2 = pisar_elemento(M, 2)         

archivo = "arbolado-en-espacios-verdes.csv"
directorio = "/home/clinux01/Documentos/labo-datos"

fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

df.head(3)
df.tail()
df.columns
df[["altura_tot","diametro"]].describe()

(df["nombre_com"] == "Ombú").sum()
df["nombre_com"].unique()

cant_ejemplares = df["nombre_com"].value_counts()
cant_ejemplares.head(10)
df_jacarandas = df[df["nombre_com"] == "Jacarandá"]
col = ["altura_tot" , "diametro", "inclinacio"]

df_jacarandas = df_jacarandas[col]

df_jacarandas.tail()

#Ejercicios
data_arboles_parques = pd.read_csv(fname)
data_jacarandas = data_arboles_parques[data_arboles_parques["nombre_com"] == "Jacarandá"]
data_palosborrachos = data_arboles_parques[data_arboles_parques["nombre_com"] == "Palo borracho rosado"]

cantidad_jacarandas = (data_jacarandas["nombre_com"].value_counts())["Jacarandá"]
#alt_max_jacaranda = 
#alt_min_jacaranda = 
#alt_prom_jacaranda = 
#diam_max_jacaranda = 
#diam_min_jacaranda =
#diam_prom_jacaranda =  

cantidad_palosborrachos = (data_palosborrachos["nombre_com"].value_counts())["Palo borracho rosado"]
#alt_max_paloborracho = 
#alt_min_paloborracho = 
#alt_prom_paloborracho = 
#diam_max_paloborracho = 
#diam_min_paloborracho =
#diam_prom_paloborracho =  