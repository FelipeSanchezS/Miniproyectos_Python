import openpyxl
import os
import pandas as pd
import seaborn
from openpyxl.styles import Font, PatterFill, Alignment

#Definimos la función de crear excel
def crear_excel_inicial():
    #Creamos un nuevo libro de trabajo
    wb = openpyxl.Workbook()
    #Creamos una hoja de trabajo activa
    ws = wb.active
    ws.title = "Inventario principal"
    #Guardamos el archivo
    wb.sabe('Inventario.xlsx')
