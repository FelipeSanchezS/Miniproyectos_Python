#Importamos librerias
import requests
import streamlit as st

api_key = ''

# Función para interactuar con la API de OpenAI
def solicitudes_openai(prompt):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers=headers,
        json={
            'prompt': prompt,
            'model': 'dall-e-3',
            'size': '1024x1024',
            'quality': 'standard',
            'n': 1
        }
    )
    if response.status_code != 200:
        error_message = response.json().get("error", {}).get("message", "Error desconocido")
        raise Exception(f"Error de la API: {error_message}")
    return response.json()['data'][0]['url']

# Función para descargar imágenes
def descarga_imagen(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# Configuración de la página
st.set_page_config(page_title="Generador de Imágenes", layout="centered")

# Aplicación Streamlit
st.title("Generador de Imágenes")

# Entrada del usuario
description = st.text_area("Describe la imagen que deseas generar:")

# Botón para generar imagen
if st.button("Generar Imagen"):
    if not description.strip():
        st.error("Por favor, ingresa una descripción válida.")
    else:
        with st.spinner("Generando imagen..."):
            try:
                url = solicitudes_openai(description)
                filename = "C:/Users/pipe-/Downloads/PruebaGenerador/generador.png"
                descarga_imagen(url, filename)
                st.image(filename, use_column_width=True)
                with open(filename, "rb") as f:
                    image_data = f.read()
                st.download_button(label="Descargar Imagen", data=image_data, file_name="imagen_generada.jpg")
            except Exception as e:
                st.error(f"Error: {e}")