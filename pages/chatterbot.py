import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# create a new chatbot
chatbot = ChatBot('Digital Assistant')

# train the chatbot on a specific corpus (in this case, the English corpus)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# define a function to get the chatbot's response to a user message
def get_response(user_message):
    return chatbot.get_response(user_message).text

# example usage
print(get_response("Hi there!"))
print(get_response("What's your name?"))
print(get_response("Can you help me with my account?"))
