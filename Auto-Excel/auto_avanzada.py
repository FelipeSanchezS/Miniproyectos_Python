#Sección de gráficos
#Importar librerías
import openpyxl
from openpyxl.styles import Font, Color, PatternFill, Border, Side
from openpyxl.chart import BarChart, Reference, LineChart, PieChart, ScatterChart
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.drawing.fill import GradientFill
from openpyxl.worksheet.datavalidation import DataValidation
import datetime
import os
import win32com.client as win32

#Creamos función para gráfico de ventas
def crear_grafico_ventas(ws):
    """Crea un gráfico de barras para las ventas por mes."""
    #creaos un gráfico de barras
    grafico = BarChart()
    grafico.title = "Cantidad de productos"
    grafico.x_axis.title = "Productos"
    grafico.y_axis.title = "Cantidad de productos"
    grafico.style = 10

    #Datos de gráfico
    datos = Reference(ws, min_col=4, min_row=1, max_row=ws.max_row, max_col=4)
    categorias = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)

    grafico.add_data(datos, titles_from_data=True)
    grafico.set_categories(categorias)

    #Añadimos grafico a la hoja
    ws.add_chart(grafico, "G2")
