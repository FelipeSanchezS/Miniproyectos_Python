from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import pandas as pd

class WordAutomation:
    def __init__(self, filename="documento_generado.docx"):
        """Inicializa un documento de Word."""
        self.filename = filename
        self.document = Document()

    def agregar_párrafo(self, texto, fuente = "Arial", tamaño = 12):
        """Agrega un párrafo en especifico"""
        p=self.document.add_paragraph(texto)
        run = p.run[0]
        run.font.name = fuente
        run.font.size = Pt(tamaño)