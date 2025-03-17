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

        #Determinamos carpeta destino
        if carpeta_destino is None:
            carpeta_destino = os.path.dirname(ruta_imagen)

        #Creamos la carpeta destino si esta no existe
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        #Creamos la ruta de salida
        formato_salida = formato_salida.lower().strip(".")
        ruta_salida = os.path.join(carpeta_destino, f"{nombre_base}.{formato_salida}")

        #Guardamos la imagen con nuevo formato
        imagen.save(ruta_salida)
        print("La imagen fue guardada y convertida en "+ruta_salida)

        return ruta_salida
    
    except Exception as e:
        print("Error al convertir la ruta "+e)
        return None

# Función para convertir varias imágenes
def convertir_multiples_imagen(carpeta_origen, formato_salida, carpeta_destino = None):
    """
    Convierte ima imagen a un formato especificado

    Args:
        carpeta_origen: Ruta de la imagen a convertir
        formato_salida: Formato al que se convertirá (ej: PNG)
        carpeta_destino: Carpeta donde se guardará la imagen convertida (Opcional)

    Returns:
        int: Número de imágenes convertidas exitosamente
    """
    #Verificamos si la carpeta existe
    if not os.path.exists(carpeta_origen):
        print("Error, la carpeta "+carpeta_destino+" No existe")
        return 0
    
    #Exenciones de imágenes mas comunes
    extensiones_imagen = ["JPG", "JPEG", "PNG", "GIF", "BMP", "TIFF", "WEBP"]

    #Contador de imágenes convertidas
    contador = 0

    #Recorremos todos los archivos de la carpeta
    for archivo in os.listdir(carpeta_origen):
        ruta_archivo = os.path.join(carpeta_origen, archivo)

        #verificar si es un archivo y tiene extensión de imagen
        if os.path.isfile(ruta_archivo) and any(archivo.lower().endswith(ext) for ext in extensiones_imagen):
            #convertir la imagen
            if convertir_imagen(ruta_archivo, formato_salida, carpeta_destino):
                contador += 1
    return contador

#Definimos la función principal
def main():
    """ Función principal del programa"""
    print("Conversor de imágenes")

    #Mostramos los formatos soportados
    listar_formatos_soportados()
    print("\n")

    #Menú de opciones
    print("Opciones:")
    print("1. Convertir una imagen")
    print("2. Convertir todas las imágenes de una carpeta")

    opción = input("\nSelecciona una opción (1 ó 2): ")

    if opción == "1":
        #convertir una imagen
        ruta_imagen = input("Ingresa la ruta de la imagen a convertir: ")
        formato_salida = input("Ingresa el formato de salida: ")
        carpeta_destino = input("Ingresa la carpeta destino (Opcional): ")

        if not carpeta_destino:
            carpeta_destino = None
        
        convertir_imagen(ruta_imagen, formato_salida, carpeta_destino)
    
    elif opción == "2":
        #convertir una imagen
        carpeta_origen = input("Ingresa la ruta de la imagen a convertir: ")
        formato_salida = input("Ingresa el formato de salida: ")
        carpeta_destino = input("Ingresa la carpeta destino (Opcional): ")

        if not carpeta_destino:
            carpeta_destino = None

        num_convertidas = convertir_multiples_imagen(carpeta_origen, formato_salida, carpeta_destino)
        print("Se convirtieron "+num_convertidas+" imágenes exitosamente. ")
    
    else:
        print("Opción no valida.")

if __name__ == "__main__":
    main()