from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

#Creamos el documento
document = Document()

#En esta parte creamos los diferentes párrafos que vayamos a necesitar
párrafo1 = document.add_paragraph()
párrafo2 = document.add_paragraph()
párrafo3 = document.add_paragraph()

#Con esto centramos el párrafo
párrafo1.alignment = WD_ALIGN_PARAGRAPH.CENTER
párrafo2.alignment = WD_ALIGN_PARAGRAPH.LEFT
párrafo3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

#Agregamos primer texto al párrafo y definimos otros estilos
run1 = párrafo1.add_run("Este es un texto") 
run1.font.name = 'Arial' #Definimos letra
run1.font.size = Pt(12) #Definimos tamaño

#Agregamos Segundo párrafo y definimos otros estilos
run2 = párrafo2.add_run("Con otro tipo de letra se diseño la segunda linea hacia la izquierda - ") 
run2.font.name = 'Times New Roman' #Definimos letra
run2.font.size = Pt(14) #Definimos tamaño
run2.font.bold = True

#Agregamos mas texto en el párrafo 2 y definimos otros estilos
run3 = párrafo2.add_run("Es la continuación de la misma segunda linea con otros estilos para seguir probando") 
run3.font.name = 'Calibri' #Definimos letra
run3.font.size = Pt(18) #Definimos tamaño
run3.font.bold = True

#Agregamos párrafo 3 y agregamos textos
run4 = párrafo3.add_run("Este es el estilo correspondiente al tercer párrafo del documento que se esta creando") 
run4.font.name = 'Georgia' #Definimos letra
run4.font.size = Pt(11) #Definimos tamaño
run4.font.color.rgb = RGBColor(0,0,255)

#Guardamos el documento
document.save("AutomatizaciónV2.docx")