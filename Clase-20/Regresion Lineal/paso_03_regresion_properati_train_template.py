# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelos de Regresion Lineal
                - Cargamos los datos de test y train de properati
                - Proponemos distintos modelos y los evaluamos
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
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
    plt.plot(x_vals, y_vals, '--', color="darkgreen")

#%%
####################################################################
########  MAIN
####################################################################
# Cargamos el archivo ya limpio
carpeta = '/home/clinux01/Descargas/Clase-20/'
data_train = pd.read_csv(carpeta+'data_alq_caba_train.csv', index_col = 'id', encoding='utf-8')


#%%
# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple 1
# ----------------------------------
# ----------------------------------
# Primer propuesta: Modelo Lineal Simple (rls) tomando a:
#  X1 = surface_total (variable predictora)
#  Y  = price         (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables
X1 = data_train[['surface_total']]
Y = data_train[['price']]

# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(X1,Y)
# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ",  rls.intercept_[0])
print("   pendiente: ", rls.coef_[0][0])


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos 
Y_pred1 = rls.predict(X1)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))


###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total
ax = sns.scatterplot(data=data_train, x='surface_total', y='price', s=5, alpha= 0.7)
ax.set_xlabel('Superficie total (m2)', fontsize=12)
ax.set_ylabel('Precio de alquiler ($ARS)', fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])
plt.title('Datos de entrenamiento \n junto con la recta de ajuste')
# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del Y, Y_pred1

#%%
# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple 2
# ----------------------------------
# ----------------------------------
# Segunda propuesta: Modelo Lineal Simple (rls) tomando a:
#  X1 = surface_covered (variable predictora)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables
X1 = data_train[['surface_covered']]
Y = data_train[['price']]
# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(X1,Y)
# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ",  rls.intercept_[0])
print("   pendiente: ", rls.coef_[0][0])


######################################
## Evaluacion del modelo contrar TRAIN
######################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

Y_pred1 = rls.predict(X1)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de puntos de precio en funcion de la superficie total
ax = sns.scatterplot(data=data_train, x='surface_covered', y='price', s=5, alpha= 0.7)
ax.set_xlabel('Superficie cubierta (m2)', fontsize=12)
ax.set_ylabel('Precio de alquiler ($ARS)', fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])
plt.title('Datos de entrenamiento \n junto con la recta de ajuste')

# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del X1, Y, Y_pred1

#%%
# ----------------------------------
# ----------------------------------
#       Modelo Multilineal 1
# ----------------------------------
# ----------------------------------
# Tercera propuesta: Modelo Multilineal tomando a:
#  X1 = surface_covered    (variable predictora 1)
#  X2 = surface_notCovered (variable predictora 2)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Declaramos las variables
data_train['surface_not_covered']=data_train['surface_total']-data_train['surface_covered']
Xs = data_train[['surface_covered', 'surface_not_covered']]
Y = data_train['price']
# Un chequeo que se podria realizar es si surface_not_covered>=0 en todos los casos

# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(Xs,Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ",  rls.intercept_)
print("   pendiente: ", rls.coef_[0])


#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

Y_pred1 = rls.predict(Xs)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))


#######################################################
## Visualizacion del modelo vs valores de entrenamiento
#######################################################
# Este tipo de modelos ya es mas dificil de visualizar

# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del Xs, Y, Y_pred1

#%% 
# ----------------------------------
# ----------------------------------
#       Modelo Multilineal 2
# ----------------------------------
# ----------------------------------
# Cuarta propuesta: Modelo Multilineal tomando a:
#  X1 = surface_covered    (variable predictora 1)
#  X2 = lat                (variable predictora 2)
#  X3 = lon                (variable predictora 2)
#  Y  = price           (variable a predecir)
########################
## Generacion del modelo
########################
# Antes de utilizar lat y lon veamos si tienen valores null
# Comenzamos con lat ...
print('Cantidad de valores null en la columna lat:', data_train['lat'].isna().sum())
# Generamos un nuevo dataframe de datos para este modelo tal que no 
# contenga na en lat
data_train_l = data_train[~data_train['lat'].isna()]
# Ahora verificamos en data_train_l si quedan registros con null en lon
print('Cantidad de valores null en la columna lon:', data_train_l['lon'].isna().sum())
# data_l ya no tiene null ni en lat ni en lon
# Declaramos las variables
Xs = data_train_l[['surface_covered', 'lat', 'lon']] # doble corchete es importante
Y  = data_train_l[['price']]
Y = data_train_l[['price']]
# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(Xs,Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ", rls.intercept_[0])
print("   pendiente: ", rls.coef_[0])


####################################
## Evaluacion del modelo contra TRAIN
#####################################  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

Y_pred1 = rls.predict(Xs)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score
rls.score(Xs, Y)


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))


#######################################################
## Visualizacion del modelo vs valores de entrenamiento
#######################################################
# Este tipo de modelos ya es mas dificil de visualizar

# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del Xs, Y, Y_pred1

#%% 
# ----------------------------------
# ----------------------------------
#       Modelo Polinomial 1
# ----------------------------------
# ----------------------------------
# Quinta propuesta: Modelo Polinomial tomando a:
#  X1    = surface_covered  (variable predictora)
#  Y     = price            (variable a predecir)
#  grado = 30
########################
## Generacion del modelo
########################
# Declaramos las variables
X1 = data_train[['surface_covered']]
Y = data_train[['price']]
grado = 30
# Generamos las variables polinomicas (Xp = [X^0,X^1,...,X^30])
pol = PolynomialFeatures(grado)
Xp = pol.fit_transform(X1)
# Declaramos el tipo de modelo
rls = linear_model.LinearRegression()
# Entrenamos el modelo
rls.fit(Xp, Y)

# Observamos los valores obtenidos (pendiente e intercept)
print("Coefficients")
print("------------")
print("   intercept: ",  rls.intercept_[0])
print("   pendiente: ", rls.coef_[0])


######################################
## Evaluacion del modelo contrar TRAIN
######################################
#  R2
# Calculamos el R2. Recordar que 1 es en el caso de una prediccion perfecta
# ... Para calcular R2 usamos los residuos de predecir los datos de test

Y_pred1 = rls.predict(Xp)
print("R^2 (train): %.2f" % r2_score(Y, Y_pred1))
# Otra manera de calcular R2, es con la funcion score


# MSE (mean squared error, o en castellano error cuadratico medio)
print("MSE (train): %.2f" % mean_squared_error(Y, Y_pred1))

# Eliminamos las variables auxiliares que ya no utilizamos
del rls
del X1, Y, Xp, Y_pred1
del grado, pol

