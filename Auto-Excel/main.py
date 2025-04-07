import openpyxl
import os
import pandas as pd
import seaborn


#Creamos un dataset de ejemplo
datos = {
    'Producto': ['Juan', 'Ana', 'Pedro', 'Maria', 'Luis'],
    'Precio': [1000, 2000, 3000, 4000, 5000],
    'Cantidad': [2, 4, 6, 8, 10]}

df = pd.DataFrame(datos)
print(df)