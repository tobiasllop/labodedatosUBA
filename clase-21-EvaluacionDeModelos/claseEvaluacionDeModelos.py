#!/usr/bin/env python
# coding: utf-8

# # Evaluación de Modelos
# 
# **Objetivo:** dada los datos de una canción (una fila en nuestro dataset) poder predecir si esta en Folklore o Evermore o es de otro álbum.
# 
# **Datos:** dataset con distintas variables de las canciones de Taylor Swift.

# In[1]:


import pandas as pd 
import utils


# #### Cargamos el dataset -- la función load_dataset limpia un poco los datos

# In[2]:


df_taylor = utils.load_dataset_taylor("archive/taylor_album_songs.csv")
df_taylor.head()


# ### Separemos los labels y eliminamos el nombre de la canción

# In[ ]:


X = df_taylor.drop(columns = ['track_name', 'is_folklore_or_evermore'])
y = df_taylor['is_folklore_or_evermore']


# In[4]:


# Complete aqui con su clasificador de preferencia!

