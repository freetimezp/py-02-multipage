import streamlit as st

def contact_form():
    with st.form("contact_form"):
        name = st.text_input(label= "First Name", placeholder="First Name")
        email = st.text_input(label= "Email Address", placeholder="Email Address")
        message = st.text_area(label= "Message", placeholder="Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success("Message successfully sent..")













