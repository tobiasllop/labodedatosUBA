# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Aprendizaje No Supervisado
Detalle     : Modelos DBSCAN
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-31
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN

#%%
####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = '~/Downloads/'
data_train = pd.read_csv(carpeta+'datos_clase_clustering.csv', index_col = 0, encoding='utf-8')

#%%
# Analizamos el precio de venta (U$S) por m2 de superficie cubierta. Para ello 
# generamos la variable ppm (precio por m2 de superficie cubierta)
data_train['ppm'] = data_train['price']/data_train['surface_covered']


#%%
# ------------------------------------------
# ------------------------------------------
#       Exploracion de Datos - Propuesta 1
# ------------------------------------------
# ------------------------------------------
# Queremos ver como es la relacion entre el precio de venta por m2 de 
# superficie cubierta (U$S) y la superficie cubierta (m2)


# Para ello visualizamos el precio de venta por m2 de superficie cubierta (U$S)
# en funcion de la superficie cubierta (m2)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm') 
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")

# Eliminamos las variables que ya no utilizamos
del ax

#%%
# ---------------------------------
# ---------------------------------
#       Modelo DBSCAN - Propuesta 1
# ---------------------------------
# ---------------------------------
#  X1 = surface_covered (variable predictora) [Superficie cubierta (m2)]
#  X2 = ppm             (variable predictora) [Precio de venta por m2 de superficie cubierta (U$S)]
#  distancia      = parametro del modelo: distancia maxima para ser vecino 
#  cantMinVecinos = parametro del modelo: cantidad minima de vecinos 
########################
## Generacion del modelo
########################
# Declaramos las variables

# Declaramos el tipo de modelo

# Entrenamos el modelo

# Asignamos las eitquetas predichas a cada fila de nuestro dataset

# Visualizamos los 3 clusters generados en funcion de su 
# superficie cubierta (m2) y el precio por m2 de la superficie cubierta (U$S)

# Eliminamos las variables que ya no utilizamos


#%%
# ------------------------------------------
# ------------------------------------------
#       Exploracion de Datos - Propuesta 2
# ------------------------------------------
# ------------------------------------------
# Queremos ver como se agrupan en relacion a la ubicacion,
# es decir, en relacion a sus coordenadas geograficas

# Para ello visualizamos cada propiedad en relacion a su latitud y longitud
ax = sns.scatterplot(data=data_train, x='lat', y= 'lon') 
ax.set_xlabel("Latitud")
ax.set_ylabel("Longitud")
plt.grid()

# Eliminamos las variables que ya no utilizamos
del ax

#%%
# ---------------------------------
# ---------------------------------
#       Modelo DBScan - Propuesta 2
# ---------------------------------
# ---------------------------------
#  X1  = latitud  (variable predictora) 
#  X2  = longitud (variable predictora) 
#  distancia      = parametro del modelo: distancia maxima para ser vecino 
#  cantMinVecinos = parametro del modelo: cantidad minima de vecinos 
########################
## Generacion del modelo
########################
# Declaramos las variables

# Declaramos el tipo de modelo

# Entrenamos el modelo

# Asignamos las eitquetas predichas a cada fila de nuestro dataset

# visualizamos los grupos generados en funcion de su ubicacion (longitud, latitud)

# Eliminamos las variables que ya no utilizamos
