import streamlit as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image

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

if st.button('Crear Factura 🤖'):
    st.image('data:image/png;base64,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')
   
    st.write('🤖 Te he creado la factura para el cliente ', cliente, 'por un monto de ', valor, ' y con una fecha de vencimiento de ', fecha_limite)

    st.button('Enviar Factura al Cliente 💰')
