import pandas as pd
import numpy as np
import streamlit as st


st.set_page_config(page_title="Riego y Fertilizacion de Plantas",
                    page_icon= "🍃")

st.title("Base de Datos")

st.dataframe(df)