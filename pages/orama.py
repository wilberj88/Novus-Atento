import streamlit as st
import pandas as pd
import numpy as np
import datetime

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Atento", page_icon="🤖")

st.title('Novus Atento 🤖 - Orama')
st.header("Asistente Virtual para tus facturas")

#CONFIGURACIÓN DE LA FACTURA
st.title('Indica de cuánto es la factura')
valor = st.slider('¿Monto en euros?', 0, 300000)

st.title('Indica a cuál cliente')
cliente = st.selectbox("Seleccione un cliente a facturar",
("Cliente A", "Cliente B", "Cliente C", "Cliente D", "Cliente E"),
)

st.title('Indica el plazo de pago')
fecha_limite = st.date_input("Cuál es la fecha de vencimiento de la factura?",
    datetime.date(2023, 6, 30))

st.title('Carga tu logo para que la factura quede perfecta')
logo = st.file_uploader("Sube tu logo en formato PNG")

if st.button('Crear Factura')
    st.write('Estamos creando la factura para el cliente ', cliente, 'por un monto de ', valor, ' y con una fecha de vencimiento de ', fecha_limite)
