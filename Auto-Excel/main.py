import openpyxl
import os
import pandas as pd
import seaborn
import mathplotlib.pyplot as plt

#Creamos un dataset de ejemplo
datos = {
    'Nombre': ['Juan', 'Ana', 'Pedro', 'Maria'],
    'Edad': [1000, 2000, 3000, 4000, 5000],
    'Ciudad': [2, 4, 6, 8, 10],}

df = pd.DataFrame(datos)
print(df)