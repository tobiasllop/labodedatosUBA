#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:31:29 2023

@author: clinux01
"""

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns


df = pd.read_csv('/home/clinux01/Descargas/datos-manos.csv')
df['Tiempo'] = pd.to_numeric(df['Tiempo'], downcast="float")
mano_derecha = df[(df['Mano']=='Derecha')]
mano_izquierda = df[(df['Mano']=='Izquierda')]

#Promedios
media_tiempo_total = df['Tiempo'].mean()
media_tiempo_derecha = mano_derecha['Tiempo'].mean()
media_tiempo_izquierda = mano_izquierda['Tiempo'].mean()
print('media der: ', media_tiempo_derecha)
print('media izq: ', media_tiempo_izquierda)
print('media tot: ', media_tiempo_total)

#Histograma
df['Tiempo'].plot(kind = 'hist').set(xlabel = 'Tiempo', ylabel='Cantidad')
plt.show()
plt.close()

#------------------------------------
# Distribucion de los datos (plot)
#------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(10, 3), sharey=True, dpi=100)
sns.distplot(df['Tiempo'], color="orange", ax=axes[0], axlabel='Tiempo (Ambas) [s]')
sns.distplot(mano_derecha['Tiempo'], color="dodgerblue", ax=axes[1], axlabel='Tiempo (Derecha) [s]')
sns.distplot(mano_izquierda['Tiempo'], color="red", ax=axes[2], axlabel='Tiempo (Izquierda) [s]')


#------------------------------------
# Separamops por mano habil y no habil
#------------------------------------

df = pd.read_csv('/home/clinux01/Descargas/datos-manos-habil.csv')
df['Mano_Habil'] = pd.to_numeric(df['Mano_Habil'], downcast="float")
df['Mano_No_Habil'] = pd.to_numeric(df['Mano_No_Habil'], downcast="float")

#Promedios
media_tiempo_total = ( df['Mano_Habil'].mean() + df['Mano_No_Habil'].mean() ) / 2 
media_tiempo_habil = df['Mano_Habil'].mean()
media_tiempo_no_habil = df['Mano_No_Habil'].mean()
print('media habil: ', media_tiempo_habil)
print('media no habil: ', media_tiempo_no_habil)
print('media tot: ', media_tiempo_total)

#Histograma
df['Mano_habil'].plot(kind = 'hist').set(xlabel = 'Tiempo', ylabel='Cantidad')
plt.show()
plt.close()
