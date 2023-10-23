# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelo de Regresion Lineal Simple
Autores     : Maria Soledad Fernandez y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from inline_sql import sql, sql_val

#%%
####################################################################
########  DEFINICION DE FUNCIONES AUXILIARES
####################################################################

# Dibuja una recta. Toma como parametros pendiente e intercept
def plotRectaRegresion(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color="red")

#%%

####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = '/home/clinux01/Descargas/Archivos-Clase-19/'
data_train = pd.read_csv(carpeta+"datos_roundup.txt", sep=" ", encoding='utf-8')


# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple (rls)
# ----------------------------------
# ----------------------------------
#  X = RU (variable predictora) [Dosis de Roundup]
#  Y = ID (variable a predecir) [Damage Index]
########################
## Generacion del modelo
########################
# Declaramos las variables
x = data_train[['RU']]
y = data_train[['ID']]


# Declaramos el tipo de modeloregresionLinealSimpleRU-template.py

rls = linear_model.LinearRegression()


# Entrenamos el modelo
rls.fit(x,y)
# Observamos los valores obtenidos (pendiente e intercept)
print(' intercept : ', rls.intercept_[0])
print(' pendiente : ', rls.coef_[0][0])

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
ax = sns.scatterplot(data=data_train, x='RU', y='ID', s=40, color='black')
ax.set_xlabel('Dosis de RU (ug/huevo)', fontsize=12)
ax.set_ylabel('Indice de daño', fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])
#####################################
## Prediccion
#####################################
# Cargamos el archivo (no posee valores para ID)
carpeta = '/home/clinux01/Descargas/Archivos-Clase-19/'
data_a_predecir = pd.read_csv(carpeta+"datos_a_predecir.txt", sep=" ", encoding='utf-8')

# Realizamos la prediccion de ID utilizando el modelo y
# la asignamos a la columna ID
data_a_predecir[['ID']] = rls.predict(data_a_predecir[['RU']])

# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
# Graficamos tanto los puntos de entrenamiento del modelo como los predichos
ax = sns.scatterplot(data=data_train, x='RU', y='ID', s=40, color='black')
ax = sns.scatterplot(data=data_a_predecir, x='RU', y='ID', s=40, color='olive')
ax.set_xlabel('Dosis de RU (ug/huevo)', fontsize=12)
ax.set_ylabel('Indice de daño', fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
Y_pred1 = rls.predict(x)
print('R2 (train): %.2f'%  r2_score(y, Y_pred1) )



#####################################
## TP
#####################################


# Cargamos el archivo 
carpeta = '/home/clinux01/Descargas/Archivos-Clase-19/'
data_train = pd.read_csv(carpeta+"datos_libreta_87122.txt", sep=" ", encoding='utf-8')

x1 = data_train[['RU']]
y1 = data_train[['ID']]

rls.fit(x1,y1)
Y_pred11 = rls.predict(x1)

print('R2 (train): %.2f'%  r2_score(y1, Y_pred11) )
print(' intercept : ', rls.intercept_[0])
print(' pendiente : ', rls.coef_[0][0])


