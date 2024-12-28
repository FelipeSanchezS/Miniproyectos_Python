import pyshorteners
import streamlit as st

# Crear un objeto de la clase Shortener
def acortar_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

# Configuración de la aplicación Streamlit
st.title("Acortador de URL")
url_input = st.text_area("Ingresa la URL que deseas acortar:")
if st.button("Acortar URL"):
    if url_input:
        shortened_url = acortar_url(url_input)
        st.success(f"URL acortada: {shortened_url}")
    else:
        st.error("Por favor, ingresa una URL válida.")