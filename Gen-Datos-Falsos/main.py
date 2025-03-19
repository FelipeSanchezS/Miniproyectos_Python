#Importamos librerías
import streamlit
from faker import fake
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