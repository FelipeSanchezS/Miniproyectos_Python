#Importamos librerías
import streamlit as st
from faker import Faker
import pandas as pd
import io

fake = Faker('es_CO')

available_fields = {
    'Nombre' : fake.name,
    'Dirección' : fake.address,
    'Correo electrónico' : fake.email,
    'Teléfono' : fake.phone_number,
    'Empresa' : fake.company,
    'Fecha' : fake.date,
    'Número de tarjeta de crédito' : fake.credit_card_number
}

def generate_fake_data(fields, num_rows):
    data = {field: [func() for _ in range(num_rows)] for field, func in fields.items()}
    return pd.Dataframe(data)

st.title('Generador de datos falsos con Faker')
st.write('Selecciona los campos que quieres generar y la cantidad de datos')

#sección de elegir los datos
selected_fields = st.multiselect('Selecciona los campos', options=list(available_fields.keys()), default=list(available_fields.keys()))
#sección de cantidad de los datos
num_rows = st.number_input('Ingrese la cantidad de datos que desea generar', min_value=1, max_value=1000, value=10)

if st.button('Generar datos'):
    #iteramos en cada uno de los datos
    selected_funcs = {field: available_fields[field] for field in selected_fields}
    #Validamos los datos seleccionados
    df = generate_fake_data(selected_funcs, num_rows)

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlswriter') as writer:
        writer.book.use_constant_memory = True
        df.to_excel(writer, index=False)
    output.seek(0)

    st.success('Datos generados con éxito!')
    st.write(df)