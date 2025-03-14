#Importamos librerías
import os
from PIL import Image

def listar_formatos_soportados():
    """Muestra los formatos de imagen soportados"""
    #Mostramos los formatos soportados
    formatos = ["JPG", "JPEG", "PNG", "GIF", "BMP", "TIFF", "WEBP"]
    print("Formatos soportados")
    for formato in formatos:
        print(f"-{formato}")
    return formatos

def convertir_imagen(ruta_imagen, formato_salida, carpeta_destino = None):
    """
    Convierte ima imagen a un formato especificado

    Args:
        ruta_imagen: Ruta de la imagen a convertir
        formato_salida: Formato al que se convertirá (ej: PNG)
        carpeta_destino: Carpeta donde se guardará la imagen convertida (Opcional)

    Returns:
        str: Ruta de imagen convertida
    """
    #Verificamos si la imagen existe
    try:
        if not os.path.exists(ruta_imagen):
            print('Error en la imagen '+ruta_imagen+', no existe')
            return None
        
        #Abrimos la imagen
        imagen = Image.open(ruta_imagen)

        #Obtener información de la imagen original
        nombre_archivo = os.path.basename(ruta_imagen)
        nombre_base = os.path.splitext(nombre_archivo)[0]