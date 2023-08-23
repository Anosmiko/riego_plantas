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

# Display the filtered DataFrame
st.dataframe(df)


### Vista Ultimo Riego por planta

# Mapping of day names in English to Spanish
day_names_mapping = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miércoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

# Create a form for users to input data for the new row
seleccion_ultimo_riego = st.selectbox(
                                "Seleccionar Planta:",
                                options=df["Planta"].unique(),
                                # index=0  # Set the default index to select the first city
                            )

# Filter the DataFrame based on the selected plant
filtered_df = df[(df["Planta"] == seleccion_ultimo_riego) & (df["Riego"] == "Si")]

primera_fila = filtered_df.sort_values(by="Fecha").head(1)
first_fecha_value = primera_fila["Fecha"].iloc[0]

st.write(f"{first_fecha_value}")






