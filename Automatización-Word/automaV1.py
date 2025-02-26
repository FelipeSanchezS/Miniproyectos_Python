from docx import Document

#Creamos nuevo documento word
document = Document()

#Agregamos un párrafo al documento
document.add_paragraph("Esta es la prueba de un párrafo automatizado con Python.")

#Guardamos el documento automatizado, podemos ingresar la ruta que deseemos
document.save("AutomatizaciónV1.docx")