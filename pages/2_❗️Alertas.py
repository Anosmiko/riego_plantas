import pandas as pd
import streamlit as st 

st.set_page_config(page_title="Riego y Fertilizacion de Plantas",
                    page_icon= "🍃")


# LECTURA CSV FORMULARIO
# =============================================================================
sheet_id = '1JcBYuaxBlGmuHVyi7FSaKChs8a49yeWWLA6SeZOEpXk'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url, usecols=[ 'Ingresar Planta', 'Ingresar Fecha', 'Estado de Humedad', '¿Se rego?', '¿Fertilización?'])
df = df.rename(columns={'Ingresar Planta': 'Planta',
                        'Ingresar Fecha': "Fecha",
                        'Estado de Humedad': 'Humedad',
                        '¿Se rego?': "Riego", 
                        '¿Fertilización?' : "Fertilización"})

# =============================================================================


# CHEQUEO PLANTAS BAJA HUMEDAD
# =============================================================================
 # Titulo
st.header("Revisar")
 
plantas_unique = df["Planta"].unique()

for planta in plantas_unique:
    ultima_inspeccion = df[df["Planta"] == planta].sort_values(by="Fecha").head(1)
    
    ultima_inspeccion_hum = ultima_inspeccion["Humedad"].iloc[0]
    ultima_inspeccion_rieg = ultima_inspeccion["Riego"].iloc[0]


    if  (ultima_inspeccion_hum <= 2) and (ultima_inspeccion_rieg == "No"):
        st.caption(f"\u2757 {planta}")
# =============================================================================

