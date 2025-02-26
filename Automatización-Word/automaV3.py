#Aca vamos a extraer datos de un archivo excel a un word
import pandas as pd
from docx import Document

#leemos el archivo
df = pd.read_excel("Libro1.xlsx")

#Creamos el documento
document = Document()

#Agregamos una tabla al documento con el numero de columnas del dataframe
table = document.add_table(rows=1, cols=len(df.columns))
hdr_cells = table.rows[0].cells

#Asignar los nombres de las columnas de la tabla
for i, column in enumerate(df.columns):
    hdr_cells[i].text = column

#Asignamos a cada fila los valores del dataframe
for index, row in df.iterrows():
    row_cells = table.add_row().cells
    for i, item in enumerate(row):
        row_cells[i].text = str(item)

document.save('Reporte-datos.docx')