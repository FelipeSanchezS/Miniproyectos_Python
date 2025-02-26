from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

#Creamos el documento
document = Document()

#Primer Párrafo - va estar centrado con diferentes estilos en el mismo párrafo
p1 = document.add_paragraph()
p2 = document.add_paragraph()

#Con esto centramos el párrafo
p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p2.alignment = WD_ALIGN_PARAGRAPH.LEFT

#Agregamos primer texto al párrafo y definimos otros estilos
run1 = p1.add_run("Este es un texto") 
run1.font.name = 'Arial' #Definimos letra
run1.font.size = Pt(12) #Definimos tamaño

#Agregamos Segunda texto al párrafo y definimos otros estilos
run2 = p2.add_run("Con otro tipo de letra se diseño la segunda linea hacia la izquierda") 
run2.font.name = 'Times New Roman' #Definimos letra
run2.font.size = Pt(14) #Definimos tamaño
run2.font.bold = True



#Guardamos el documento
document.save("AutomatizaciónV2.docx")