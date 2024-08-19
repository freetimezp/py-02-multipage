import re
import streamlit as st
import requests

# --- webhook from pabbly ---
WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

# --- form validation ---
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input(label= "First Name", placeholder="First Name")
        email = st.text_input(label= "Email Address", placeholder="Email Address")
        message = st.text_area(label= "Message", placeholder="Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later..")
                st.stop()
            
            if not name:
                st.error("Please provide your name..")
                st.stop()
            if not email:
                st.error("Please provide your email..")
                st.stop()
            if not is_valid_email(email):
                st.error("Please provide a valid email..")
                st.stop()
            if not message:
                st.error("Please provide message..")
                st.stop()

            # --- prepare data payload and send it to the webhook url ---
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has sent successfully..")
            else:
                st.error("Error while sending message..")












