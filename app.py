import pandas as pd
from datetime import datetime
import streamlit as st 


st.set_page_config(page_title="Riego y Fertilizacion de Plantas",
                    page_icon= "🍃")


############# LECTURA CSV FORMULARIO
sheet_id = '1JcBYuaxBlGmuHVyi7FSaKChs8a49yeWWLA6SeZOEpXk'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url, usecols=[ 'Ingresar Planta', 'Ingresar Fecha', 'Estado de Humedad', '¿Se rego?', '¿Fertilización?'])
df = df.rename(columns={'Ingresar Planta': 'Planta',
                        'Ingresar Fecha': "Fecha",
                        'Estado de Humedad': 'Humedad',
                        '¿Se rego?': "Riego", 
                        '¿Fertilización?' : "Fertilización"})





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
        st.caption(f"- Revisar {planta}")
# =============================================================================



# ULTIMO RIEGO O FERTILIZACÓN PLANTA
# =============================================================================

# Define mappings for Spanish day and month names
spanish_days = {
     1: "lunes", 2: "martes", 3: "miércoles", 4: "jueves", 5: "viernes",
     6: "sábado", 7: "domingo"
 }

spanish_months = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
    7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}

def utima_accion(str_accion, key):
    # Titulo
    st.header(str_accion)
    
    # Seleccion de Planta
    seleccion_ultimo_riego = st.selectbox(
                                            "Seleccionar Planta:",
                                            options=df["Planta"].unique(),
                                            key = key
                                        )

    # Se filtra df segun seleccion
    filtered_df = df[(df["Planta"] == seleccion_ultimo_riego) & (df[str_accion] == "Si")]
    primera_fila = filtered_df.sort_values(by="Fecha").head(1)
    
    try:
        # Se obtiene fecha del ultimo riego o fertilizacipon de la planta
        ultima_fecha = pd.to_datetime(primera_fila["Fecha"].iloc[0])
        ultima_fecha = ultima_fecha.date()
        
        mes = ultima_fecha.month
        dia = ultima_fecha.day
        
       
        # Se usan los nombres en español
        spanish_day_name = spanish_days.get(ultima_fecha.weekday() + 1)
        spanish_month_name = spanish_months.get(mes)
        
        # Se obtiene fecha actual
        hoy = datetime.today().date()
        
        # Se obtiene diferencia de dias desde utlimo riego
        dias_desde_ult_riego = (hoy - ultima_fecha).days
        
        st.write(f"El ultimo {str_accion} de {seleccion_ultimo_riego} fue el dia {spanish_day_name} {dia} de {spanish_month_name}, hace {dias_desde_ult_riego} dias.")

    except IndexError:
        st.write("No hay registros")
        
    

utima_accion("Riego", "Riego")
utima_accion("Fertilización", "Fertilización")

# =============================================================================












