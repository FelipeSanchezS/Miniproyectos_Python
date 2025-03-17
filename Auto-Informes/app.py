#Importamos librerías
import streamlit as st
import pandas as pd
from docx import Document
from docx.shared import Inches
import matplotlib as plt
import io
import openpyxl

def main():
    #titulo
    st.title("Generador de informes mediante python")
    #Acá se pone para cargar la plantilla word
    template_file = st.file_uploader("Cargue su plantilla Word", type="docx")

    #Acá se pone para cargar la el archivo de excel ocn la información
    data_file = st.file_uploader("Cargue sus datos", type=["xlsx", "cvs"])

    if template_file and data_file:
        st.success("Archivos cargados de forma correcta")

        #Cargamos el archivo con los datos que se subieron desde el pc
        # se usa el read cvs si es .cvs, pero si es excel se usa el read_excel
        df = pd.read_csv(data_file) if data_file.name.endswith('.csv') else pd.read_excel(data_file) 

        #creamos encabezado
        st.subheader("Datos cargados")
        #Mostramos los datos que están en el dataset
        st.dataframe(df)

main()