import pandas as pd
import requests
import streamlit as st 

### LECTURA CSV FORMULARIO
sheet_id = '1JcBYuaxBlGmuHVyi7FSaKChs8a49yeWWLA6SeZOEpXk'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url, usecols=[ 'Ingresar Planta', 'Ingresar Fecha', 'Estado de Humedad', '¿Se rego?', '¿Fertilización?'])
df = df.rename(columns={'Ingresar Planta': 'Planta',
                        'Ingresar Fecha': "Fecha",
                        'Estado de Humedad': 'Humedad',
                        '¿Se rego?': "Riego", 
                        '¿Fertilización?' : "Fertilización"})


### Vista Ultimo Riego por planta
# Create a form for users to input data for the new row
seleccion_ultimo_riego = st.selectbox(
                                "Seleccionar Planta:",
                                options=df["Planta"].unique(),
                                # index=0  # Set the default index to select the first city
                            )

st.dataframe(df[seleccion_ultimo_riego]) 




