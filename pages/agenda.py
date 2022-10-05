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
  - 🔎 _    Controlar tus metas y horarios diarios, desde el despertar hasta el acostar
  - 🛒 _    Alarmar cumplimiento de metas diarias, semanales y mensuales
  - ✍️ _     Recomendaciones para sa
  
  CONFIGURA TU ATENTO 🤖 AHORA 🕰
  """
)


i = st.radio('Indícanos tu cepas preferidas:', ['Orange', 'Gorila Kush', 'Gorila Og', 'PuntoRojo', 'IRE', 'Amazonas'])

if a and b and c:
  st.write('Muchas gracias, ', d, e, 'Enviamos un correo de confirmación a  <<',a, '>>. Estamos preparando el envío de tu Julito hacia la ciudad de <<', b, '>> a la dirección: <<', c, '>>.')


st.button('Crear mi Atento 🤖 Agenda exclusivo para mí')
