#Importamos librerias
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

#Creamos el documento
document = Document()

#Ingresamos los datos necesarios
nombre = input('Ingrese su nombre: ')
dirección = input('Ingrese su dirección de residencia: ')
email = input('Ingrese su correo: ')
teléfono = input('Ingrese su teléfono: ')
fechaA = input('Ingrese la fecha: ')
empresa = input('Ingrese nombre de la empresa: ')
ciudadPaís = input('Ingrese ciudad y país: ')
cargo = input("Ingrese su cargo desempeñado: ")
fechaF = input("Ingrese la fecha de efectividad de la renuncia: ")

#------Primera linea-------
párrafo1 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo1.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo1.add_run(nombre) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)
run.font.italic = True

#------Segunda linea-------
párrafo2 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo2.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo2.add_run(dirección) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)
run.font.italic = True

#------Tercera linea-------
párrafo3 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo3.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo3.add_run(email) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)
run.font.italic = True

#------Cuarta linea-------
párrafo4 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo4.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo4.add_run(teléfono) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)
run.font.italic = True

#------Quinta linea-------
párrafo5 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo5.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo5.add_run(fechaA) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)
run.font.italic = True

#------Salto de linea-------
document.add_paragraph()

#------Sexta linea-------
párrafo6 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo6.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo6.add_run(empresa) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)
run.font.italic = True

#------Séptima linea-------
párrafo7 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo7.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo7.add_run(ciudadPaís) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)
run.font.italic = True

#------Salto de linea-------
document.add_paragraph()

#------Octava linea-------
párrafo7 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo7.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo7.add_run("Estimado/a "+empresa+": ") 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11)

#------Primer párrafo de la carta-------
párrafo7 = document.add_paragraph()
#Con esto elegimos dirección del párrafo el párrafo
párrafo7.alignment = WD_ALIGN_PARAGRAPH.LEFT
#Agregamos párrafo 4 y agregamos textos
run = párrafo7.add_run("Por medio de la presente, me dirijo a usted para presentar mi renuncia al cargo "+ cargo +" en "+ empresa +", con efectividad a partir del "+ fechaF) 
run.font.name = 'Arial' #Definimos letra
run.font.size = Pt(11) #Definimos tamaño



#Guardamos el documento
document.save("Carta_Renuncia "+nombre+".docx")