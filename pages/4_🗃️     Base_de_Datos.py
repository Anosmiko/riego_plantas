import pandas as pd
import numpy as np
import streamlit as st


st.set_page_config(page_title="Riego y Fertilizacion de Plantas",
                    page_icon= "🍃")

st.title("Base de Datos")

# LECTURA CSV FORMULARIO
# =============================================================================
sheet_id = '1JcBYuaxBlGmuHVyi7FSaKChs8a49yeWWLA6SeZOEpXk'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url, usecols=[ 'Ingresar Planta', 'Ingresar Fecha', '¿Se rego?', '¿Fertilización?'])
df = df.rename(columns={'Ingresar Planta': 'Planta',
                        'Ingresar Fecha': "Fecha",
                        '¿Se rego?': "Riego", 
                        '¿Fertilización?' : "Fertilización"})


date_format = "%d/%m/%Y"

df["Fecha"] = pd.to_datetime(df['Fecha'], format=date_format)
df = df.sort_values(by="Fecha", ascending=False)
df.reset_index(drop=True, inplace=True)

# =============================================================================


st.dataframe(df)