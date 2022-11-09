import streamlit as st
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration

@st.experimental_singleton
def get_models():
  model_name = "facebook/blenderbot-400M-distill"
  tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
  model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
  return tokenizer, model

if "history" not in st.session_state:
  st.session_state.history = []
  
st.title("Conócete con Atento Bot")

def generate_answer():
  tokenizer, model = get_models()
  user_message = st.session_state.input_text
  inputs = tokenizer(st.session_state.input_text, return_tensor="pt")
  result = model.generate(**inputs)
  message_bot = tokenizer.decode(
    result[0], skip_special_tokens=True)
  st.session_state.history.append({"message": user_message, "is_user":True})
  st.session_state.history.append({"message": message_bot, "is_user":False})

st.text_input("Habla con Atento Bot", key="input_text", on_change=generate_answer)

for chat in st.session_state.history:
  st_message(**chat)

 
