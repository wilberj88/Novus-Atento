import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Atento", page_icon="🤖")

st.title('Novus Atento 🤖')
st.header("Configura tu Atento 🗓️ Agenda 📆")

st.markdown(
  """
  Novus Atento Agenda te apoyará en:
  - 🔎 _    Controlar tu meta mensual y anual
  - ⏰ _    Analizar tu cumplimiento de tus metas
  - ✅ _     Aconsejar sobre tu proceso de mejora
  
  CONFIGURA TU ATENTO 🤖 AHORA 🕰
  """
)


meta_ingreso = st.slider('¿Cuál es tu meta de generación de ingresos en 2023?', 0, 100000)

meta_ejercicio = st.radio('¿Cuál es tu meta de realización de ejercicio en 2023?', ['2 días a la semana', '3  días a la semana', '4 días a la semana', '5  días a la semana', '6 días a la semana'])

meta_salud = st.radio('¿Cuántos controles médicos te harás en 2023?', ['Anual', 'Semestral', 'Trimestral'])

a = st.button('Crear mi Atento 🤖 Agenda exclusivo para mí')

if meta_ingreso and meta_ejercicio and meta_salud and a:
  st.write('Muchas gracias, Pepito Perez: hemos creado un Atento entrenado para apoyarte a conseguir tus metas, iniciando por facturar en 2023', meta_ingreso, 'ejercitarte ', meta_ejercicio, 'y cuidarte ', meta_salud)


