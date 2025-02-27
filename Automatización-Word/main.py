from automaV4 import WordAutomation

#creamos una instancia de la biblioteca
doc = WordAutomation("Reporte_automatizado.docx")

#Agregamos párrafo con formato
doc.agregar_párrafo("Este es un reporte automatizado generado con python.", fuente='Calibri', tamaño=14)

#Agregamos tabla desde un archivo excel
doc.agregar_tabla_desde_excel('Libro1.xlsx')

#Guardamos documento
doc.guardar_documento()