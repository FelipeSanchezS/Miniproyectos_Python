import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import datetime

def cargar_inventario():
    try:
        # Cargar el archivo de Excel existente
        wb = openpyxl.load_workbook('Inventario.xlsx')
        ws = wb.active
        return wb, ws
    except FileNotFoundError:
        print("El archivo 'Inventario.xlsx' no existe. Creando uno nuevo.")
        return None