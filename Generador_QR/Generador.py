import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Configuración de la aplicación Streamlit
st.title("Generador de Código QR para URLs")
st.markdown("Ingrese una URL y genere un código QR que redirija a la URL ingresada.")

# Entrada de URL
url_input = st.text_input("Ingrese la URL:", placeholder="https://ejemplo.com")

# Generar código QR
if st.button("Generar Código QR"):
    if url_input:
        try:
            # Crear el código QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url_input)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Convertir la imagen a formato para Streamlit
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            # Mostrar el código QR
            st.image(buffer, caption="Código QR generado", use_column_width=True)
            st.success("¡Código QR generado con éxito! Escanéalo para ir a la URL.")
        except Exception as e:
            st.error(f"Error al generar el código QR: {e}")
    else:
        st.warning("Por favor, ingrese una URL válida.")
