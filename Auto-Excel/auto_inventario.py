import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import datetime

def cargar_inventario():
    try:
        # Cargar el archivo de Excel existente
        wb = openpyxl.load_workbook('Inventario.xlsx')
        #return wb, ws
    except FileNotFoundError:
        print("El archivo 'Inventario.xlsx' no existe. Creando uno nuevo.")
        return None
    
    ws = wb.active
    ws.title = 'Inventario principal'

    #Aplicamos formato a los encabezados
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="0000FF", end_color="0000FF", fill_type="solid")
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = openpyxl.styles.Border(
            left=openpyxl.styles.Side(style='thin', color='000000'),
            right=openpyxl.styles.Side(style='thin', color='000000'),
            top=openpyxl.styles.Side(style='thin', color='000000'),
            bottom=openpyxl.styles.Side(style='thin', color='000000')
        )
    return wb, ws


def actualizar_precios(ws, precios):
    """Actualizar los precios de los productos en el inventario"""
    for row in ws.iter_rows(min_row=2, max_col=2, values_only=True):
        producto = row[0]
        if producto in precios:
            ws.cell(row=row[0].row, column=2).value = precios[producto]
            ws.cell(row=row[0].row, column=2).font = Font(color="FF0000")


def automatizacion_inventario():
    """Función para automatizar las operaciones que realiza el inventario"""
    wb, ws = cargar_inventario()
    if not wb:
        return
    
    wb.save('InventarioV2.xlsx')
    print("El archivo 'InventarioV2.xlsx' ha sido creado y guardado exitosamente.")

if __name__ == "__main__":
    automatizacion_inventario()

