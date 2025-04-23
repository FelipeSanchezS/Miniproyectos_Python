#Importamos la información del primer archivo py
import Crear_informe
from Crear_informe import crear_excel_inicial
from auto_inventario import automatizacion_inventario
from auto_avanzada import automatizacion_avanzada

crear_excel_inicial()
automatizacion_inventario()
automatizacion_avanzada()
#Se importan las funciones de los otros archivos py