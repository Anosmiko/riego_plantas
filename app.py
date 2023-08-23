import pandas as pd
from datetime import datetime
import streamlit as st 


st.set_page_config(page_title="Dashboard de Ventas",
                    page_icon= "🍃",
                    layout="wide")



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
# Define mappings for Spanish day and month names
spanish_days = {
    1: "lunes", 2: "martes", 3: "miércoles", 4: "jueves", 5: "viernes",
    6: "sábado", 7: "domingo"
}

spanish_months = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
    7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}


# Get today's date
hoy = datetime.today().date()

def utima_accion(str_accion, key):
    # Create a form for users to input data for the new row
    seleccion_ultimo_riego = st.selectbox(
                                            "Seleccionar Planta:",
                                            options=df["Planta"].unique(),
                                            key = key
                                            # index=0  # Set the default index to select the first city
                                        )
            
    # Filter the DataFrame based on the selected plant
    filtered_df = df[(df["Planta"] == seleccion_ultimo_riego) & (df[str_accion] == "Si")]
    
    primera_fila = filtered_df.sort_values(by="Fecha").head(1)
    
    try:
        ultima_fecha = pd.to_datetime(primera_fila["Fecha"].iloc[0])
        
        ultima_fecha = ultima_fecha.date()
        
        mes = ultima_fecha.month
        dia = ultima_fecha.day
        
        
        # Get the Spanish day and month names
        spanish_day_name = spanish_days.get(ultima_fecha.weekday() + 1)
        spanish_month_name = spanish_months.get(mes)
        
        dias_desde_ult_riego = (hoy - ultima_fecha).days
        
        st.write(f"El ultimo {str_accion} de la {seleccion_ultimo_riego} fue el dia {spanish_day_name} {dia} de {spanish_month_name}, hace {dias_desde_ult_riego} dias.")

    except IndexError:
        st.write("No hay registros")
        
    

utima_accion("Riego", "Riego")
utima_accion("Fertilización", "Fertilización")
# st.write(hoy - first_fecha_value).days()

#finds the first occurrence of today's date and changes its color 


# st.write(f"{año} {mes} {dia}")






