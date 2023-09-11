import pandas as pd
from datetime import datetime
import streamlit as st 


st.set_page_config(page_title="Riego y Fertilizacion de Plantas",
                    page_icon= "🍃")

st.title("Revisíon")
# st.sidebar.success("Seleccionar ")


# LECTURA CSV FORMULARIO
# =============================================================================
sheet_id = '1JcBYuaxBlGmuHVyi7FSaKChs8a49yeWWLA6SeZOEpXk'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

df = pd.read_csv(url, usecols=[ 'Ingresar Planta', 'Ingresar Fecha', 'Estado de Humedad', '¿Se rego?', '¿Fertilización?', '¿Asedio?'])
df = df.rename(columns={'Ingresar Planta': 'Planta',
                        'Ingresar Fecha': "Fecha",
                        'Estado de Humedad': 'Humedad',
                        '¿Se rego?': "Riego", 
                        '¿Fertilización?' : "Fertilización",
                        '¿Asedio?': 'Insecticida'})


date_format = "%d/%m/%Y"

df["Fecha"] = pd.to_datetime(df['Fecha'], format=date_format)

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


# Info por planta


# Seleccion de Planta

seleccion_planta = st.selectbox(
                                        "Seleccionar Planta:",
                                        options= sorted(df["Planta"].unique()),
                                        key = "planta"
                                    )


acciones = ["Riego", "Fertilización", "Insecticida"]

def print_info(seleccion_planta, ultima_fecha_accion, accion):
    try:
        # Se obtiene fecha del ultimo riego o fertilizacipon de la planta
        ultima_fecha_accion = ultima_accion.iloc[0]
        ultima_fecha = ultima_fecha_accion.date()
        
        mes = ultima_fecha.month
        dia = ultima_fecha.day
        
        # Se usan los nombres en español
        spanish_day_name = spanish_days.get(ultima_fecha.weekday() + 1)
        spanish_month_name = spanish_months.get(mes)
        
        # Se obtiene fecha actual
        hoy = datetime.today().date()
        
        # Se obtiene diferencia de dias desde utlimo riego
        dias_desde_ult_riego = (hoy - ultima_fecha).days
        
        if accion == "Riego":
            st.subheader('💧 RIEGO')
            st.write(f"El ultimo riego de <b>{seleccion_planta}</b> fue el dia  <b>{spanish_day_name} {dia} de {spanish_month_name}</b>, hace  <b>{dias_desde_ult_riego} dias.</b>", unsafe_allow_html=True)
            
        elif accion == "Insecticida":
            st.subheader('🐛 INSECTICIDA')
            st.write(f"La ultima aplicacion de Asedio en <b>{seleccion_planta}</b> fue el dia  <b>{spanish_day_name} {dia} de {spanish_month_name}</b>, hace  <b>{dias_desde_ult_riego} dias.</b>" , unsafe_allow_html=True)
            
        elif accion == "Fertilización":
            st.subheader('🧪 FERTILIZACIÓN')
            st.write(f"La última fertilización de <b>{seleccion_planta}</b> fue el día <b>{spanish_day_name} {dia} de {spanish_month_name}</b> , hace  <b>{dias_desde_ult_riego} días.</b>", unsafe_allow_html=True)

            
    except IndexError:
	if accion == "Riego":
            st.subheader('💧 RIEGO')
      	    st.write("No hay registros")

	elif accion == "Insecticida":
            st.subheader('🐛 INSECTICIDA')
      	    st.write("No hay registros")
	
	elif accion == "Fertilización":
            st.subheader('🧪 FERTILIZACIÓN')
	    st.write("No hay registros")


        pass


for accion in acciones:
    # Ultimo 
    ultima_accion = df["Fecha"][(df["Planta"] == seleccion_planta) & (df[accion] == "Si")]   
    ultima_accion = ultima_accion.sort_values(ascending=False).head(1)
    
    try:
        print_info(seleccion_planta, ultima_accion, accion)
    except IndexError:
        st.write("No hay registros")
    