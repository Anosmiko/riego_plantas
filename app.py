import pandas as pd
import requests
from datetime import datetime
import calendar
import streamlit as st 

############# LECTURA CSV FORMULARIO
sheet_id = '1JcBYuaxBlGmuHVyi7FSaKChs8a49yeWWLA6SeZOEpXk'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url, usecols=[ 'Ingresar Planta', 'Ingresar Fecha', 'Estado de Humedad', '¿Se rego?', '¿Fertilización?'])
df = df.rename(columns={'Ingresar Planta': 'Planta',
                        'Ingresar Fecha': "Fecha",
                        'Estado de Humedad': 'Humedad',
                        '¿Se rego?': "Riego", 
                        '¿Fertilización?' : "Fertilización"})


# Display the filtered DataFrame
st.dataframe(df)


### Vista Ultimo Riego por planta

# Get today's date
hoy = datetime.today().date()

# Create a form for users to input data for the new row
seleccion_ultimo_riego = st.selectbox(
                                "Seleccionar Planta:",
                                options=df["Planta"].unique(),
                                # index=0  # Set the default index to select the first city
                            )

# Filter the DataFrame based on the selected plant
filtered_df = df[(df["Planta"] == seleccion_ultimo_riego) & (df["Riego"] == "Si")]

primera_fila = filtered_df.sort_values(by="Fecha").head(1)
ultima_fecha = pd.to_datetime(primera_fila["Fecha"].iloc[0])
ultima_fecha = ultima_fecha.date()

mes = ultima_fecha.month
dia = ultima_fecha.day

dias_desde_ult_riego = (hoy - ultima_fecha).days

st.write(f"El ultimo riego de la {seleccion_ultimo_riego} fue el {dia} de {mes}, hace {dias_desde_ult_riego} dias.")


# st.write(hoy - first_fecha_value).days()

#finds the first occurrence of today's date and changes its color 


# st.write(f"{año} {mes} {dia}")






