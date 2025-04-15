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