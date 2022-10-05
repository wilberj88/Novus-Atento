import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Atento", page_icon="🤖")

st.title('Novus Atento 🤖')
st.header("Potencia tu vida con un Asistente Virtual personalizado para ti 🎯")

st.selectbox('Elige el rol más demandado a futuro que desees abordar', ['Data Scientist', 'Broker', 'ML Operator'])
st.multiselect('Selecciona los problemas del planeta que deseas enfrentar', ['Hambre', 'Pobreza', 'Educacion'])
st.multiselect('Selecciona tus principales pasatiempos', ['Leer', 'Ejercicio', 'Cine'])
st.text_input('Indícanos actualmente en qué te ganas la vida')


st.button('Preparar Mando de Novus Vita exclusivo para mí')



st.write("Formulario de Registro✍")
    

d = st.text_input('Nombre')

e = st.text_input('Apellido')

a = st.text_input('1. Correo electrónico')

b = st.text_input('2. Ciudad ')

c = st.text_input('3. Dirección?')

f = st.write("Adicionalmente, cuéntanos:")

g = st.slider('¿cuántos Julitos ☘️ te fumas al mes', 0, 100)

h = st.slider('¿Cuánto te cuestan todos los julitos del mes?', 0, 250000)

i = st.radio('Indícanos tu cepas preferidas:', ['Orange', 'Gorila Kush', 'Gorila Og', 'PuntoRojo', 'IRE', 'Amazonas'])

if a and b and c:
  st.write('Muchas gracias, ', d, e, 'Enviamos un correo de confirmación a  <<',a, '>>. Estamos preparando el envío de tu Julito hacia la ciudad de <<', b, '>> a la dirección: <<', c, '>>.')


picture = st.camera_input("Sonríe para nuestro registro")

if picture:
    st.image(picture)
    st.write('Bienvenido a la comunidad de Julitos☘️. Ya eres parte de nuestro parche. REPORTE DE USUARIO: consumo mensual en Julitos es de <<',g, '>>, en presupuesto es de <<',h, '>> y su cepa preferida es <<',i, '>>')

