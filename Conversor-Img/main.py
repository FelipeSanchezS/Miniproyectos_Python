#Importamos librerías
import os
from PIL import Image

def listar_formatos_soportados():
    """Muestra los formatos de imagen soportados"""
    formatos = ["JPG", "JPEG", "PNG", "GIF", "BMP", "TIFF", "WEBP"]
    print("Formatos soportados")
    for formato in formatos:
        print(f"-{formato}")
    return formatos