# Image Generation Web Application

Este proyecto es una aplicación web construida en Python que utiliza la API de OpenAI, incluyendo DALL·E 3, para generar imágenes a partir de descripciones de texto proporcionadas por los usuarios.

## Descripción

La aplicación permite que los usuarios ingresen una descripción detallada de una imagen que desean crear. Luego, la aplicación hace uso de la API de OpenAI para procesar la solicitud y generar la imagen solicitada utilizando el modelo DALL·E 3. La imagen generada es luego presentada al usuario en la interfaz web.

## Características

- Interfaz web simple y amigable.
- Generación de imágenes mediante la API de OpenAI DALL·E 3.
- Permite que los usuarios ingresen descripciones personalizadas para la creación de imágenes.
- Muestra la imagen generada al instante.

## Tecnologías

- Python
- Flask (Framework web)
- OpenAI API (DALL·E 3)
- streamlit

## Requisitos

- Python 3.7 o superior
- Instalar las dependencias listadas en el archivo `requirements.txt`
- Cuenta de OpenAI con acceso a la API de DALL·E 3

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tuusuario/imagen-generada-por-ia.git
    cd imagen-generada-por-ia
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Obtén tu clave de API de OpenAI:

   - Ve a [OpenAI](https://platform.openai.com/signup) y crea una cuenta si no tienes una.
   - Genera una clave de API en [la sección de API](https://platform.openai.com/account/api-keys).

4. Configura tu clave de API:

    - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

      ```env
      OPENAI_API_KEY=tu_clave_de_api_aqui
      ```

5. Ejecuta la aplicación:

    ```bash
    python app.py
    ```

6. Abre tu navegador y ve a `http://127.0.0.1:5000` para usar la aplicación.

## Uso

1. En la página principal de la aplicación, ingresa una descripción detallada de la imagen que deseas generar.
2. Haz clic en "Generar Imagen".
3. La aplicación enviará la solicitud a la API de OpenAI y mostrará la imagen generada en la pantalla.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar la aplicación, siéntete libre de abrir un pull request o un issue.


