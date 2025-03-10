# Proyecto de Automatización de Carta de Renuncia

Este proyecto es un script en Python que automatiza la creación de una carta de renuncia para un cargo en una empresa. El script solicita ciertos datos del usuario (como su nombre, dirección, correo electrónico, entre otros) y genera un documento `.docx` con una carta de renuncia personalizada. Este proyecto hace uso de la librería `python-docx`, que permite crear y modificar documentos Word, y proporciona la capacidad de personalizar el formato del texto (tipo de letra, tamaño, estilo, etc.).


## ¿Cómo funciona?


El usuario ejecuta el script y se le solicita ingresar una serie de datos en la consola. Los datos solicitados son los siguientes:

Nombre completo

Dirección de residencia

Correo electrónico

Teléfono

Fecha (de la carta)

Nombre de la empresa

Ciudad y país

Cargo desempeñado

Fecha de efectividad de la renuncia

Con base en esta información, el programa genera una carta de renuncia en formato .docx automáticamente.

El archivo .docx generado se guarda en la misma carpeta donde se ejecutó el script.

El script personaliza el documento de acuerdo con las preferencias del usuario, permitiendo cambiar el tipo de letra, tamaño y estilo del texto.

Librerías utilizadas
python-docx: Esta librería permite crear, modificar y personalizar documentos de Word (.docx).
docx.shared.Pt: Permite establecer el tamaño del texto.
docx.shared.RGBColor: Permite cambiar el color del texto.
docx.enum.text.WD_ALIGN_PARAGRAPH: Permite alinear el texto en el documento.

## Requisitos

Para ejecutar este proyecto, es necesario tener Python instalado en tu sistema. Además, debes instalar la librería `python-docx`, que puedes instalar utilizando el siguiente comando:

```bash
pip install python-docx

