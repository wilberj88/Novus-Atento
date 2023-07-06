import streamlit as st
import numpy as np

st.title('Novus Atento 🤖 tu mayordomo digital')
with st.chat_message("user"):
    st.write("👋Bienvenido a Novus Atento 🤖: dime ¿cómo te puedo atender hoy?")

prompt = st.chat_input("Tienes 30 segundos para tu respuesta...")
if prompt:  
    st.write(f"User has sent the following prompt: {prompt}")
