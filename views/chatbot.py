import streamlit as st
import random
import time

def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Check out my fun YouTube channel 'Studio Freetime': https://www.youtube.com/@lifelovelaugh9740!",
            "Hi! What's up? Don't forget to subscribe to 'Studio Freetime': https://www.youtube.com/@lifelovelaugh9740!",
            "Hello! Need assistance? My YouTube channel 'Studio Freetime' is full of great tips: https://www.youtube.com/@lifelovelaugh9740!",
            "Hey! Got a question? Also, subscribe to 'Studio Freetime' for awesome tutorials: https://www.youtube.com/@lifelovelaugh9740!",
            "Hi there! How can I help? BTW, my channel 'Studio Freetime' is super cool: https://www.youtube.com/@lifelovelaugh9740!",
            "Hello! Looking for help? Check out 'Studio Freetime' on YouTube: https://www.youtube.com/@lifelovelaugh9740!",
            "Hey! Need assistance? 'Studio Freetime' YouTube channel has you covered: https://www.youtube.com/@lifelovelaugh9740!",
            "Hi! Got any coding questions? Don't forget to watch 'Studio Freetime': https://www.youtube.com/@lifelovelaugh9740!",
            "Hello! Need help? 'Studio Freetime' on YouTube is a must-see: https://www.youtube.com/@lifelovelaugh9740!",
            "Hey there! Any questions? My channel 'Studio Freetime' rocks: https://www.youtube.com/@lifelovelaugh9740!",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Chatbot")


# --- initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- display chat messages from history on app rerun ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- accept user input ---
if prompt := st.chat_input("What is up?"):
    # --- add user message to chat history ---
    st.session_state.messages.append({ "role": "user", "content": prompt })
    # --- display user message in chat message container ---
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # --- display assistant response in chat message container ---
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # --- add assistant response to chat history ---
    st.session_state.messages.append({ "role": "assistant", "content": response })








