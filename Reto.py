import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importar datos de pydataset
#Checar bases de datos
#data()
#df = data('iris')
#Cargar base de datos
df = sns.load_dataset('iris')
df.head()
df.describe()
df.columns
#Ejemplos por especies
df['species'].value_counts()
#Barplot Seabron
sns.countplot(x = 'species', data = df).set_title('Conteo Especies Iris')
#Areaplot para cada variable
df.plot.area().set_title('Areaplot de Iris')
