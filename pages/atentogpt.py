import streamlit as st
import numpy as np
import random
import time

st.title('Novus Atento 🤖 tu mayordomo digital')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["user"]):
        st.markdown(message["👋Bienvenido a Novus Atento 🤖: dime ¿cómo te puedo atender hoy?"])
# React to user input
if prompt := st.chat_input("Dímelo de una"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

