import openpyxl
import os
import pandas as pd
import seaborn
from openpyxl.styles import Font, PatternFill, Alignment

#Definimos la función de crear excel
def crear_excel_inicial():
    #Creamos un nuevo libro de trabajo
    wb = openpyxl.Workbook()
    #Creamos una hoja de trabajo activa
    ws = wb.active
    ws.title = "Inventario principal"
    #Guardamos el archivo
    wb.save('Inventario.xlsx')

if __name__ == '__main__':
    #Verificamos si el archivo existe
    if not os.path.exists('Inventario.xlsx'):
        crear_excel_inicial()
        print("Archivo creado")
    else:
        print("El archivo ya existe")