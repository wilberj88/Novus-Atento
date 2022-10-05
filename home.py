import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Atento", page_icon="🤖")

st.title('Novus Atento 🤖')
st.header("Asistentes Virtuales para tus necesidades 🧘")

st.write("Cada frente de la vida tiene su magia, regístrate y elije el mejor 🧙‍ Mago 🤖 para ti")


st.write("Formulario de Registro✍")
    
d = st.text_input('Nombre')

e = st.text_input('Apellido')

a = st.text_input('1. Correo electrónico')

b = st.text_input('2. Ciudad ')

c = st.text_input('3. Dirección?')

i = st.radio('¿Cuál Atento necesitas?:', ['Atento Agenda', 'Atento Clientes', 'Atento Salud', 'Atento Trabajo', 'Atento Todos'])

if a and b and c:
  st.write('Muchas gracias, ', d, e, 'Enviamos un correo de confirmación a  <<',a, '>>. Enviaremos la facturación hacia la ciudad de <<', b, '>> a la dirección: <<', c, '>>.')


picture = st.camera_input("Sonríe para nuestro registro")

if picture:
    st.image(picture)
    st.write('Bienvenido a la comunidad de Atento🤖')
