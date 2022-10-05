import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Atento", page_icon="🤖")

st.title('Novus Atento 🤖')
st.header("Asistentes Virtuales para tus necesidades 🧘")

st.write("Cada frente de la vida tiene su magia, elije el mejor 🧙‍ Mago 🤖 para ti")

st.selectbox('Elige el Atento que requieras', ['Atento Agenda', 'Atento Clientes', 'Atento Trabajo', 'Atento Salud'])

