import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- hero section ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/images/avatar.jpg", width=230)

with col2:
    st.title("Web Developer", anchor=False)
    st.write(
        "Frontend & Backend Developer from Ukraine, simply dummy text of the printing and typesetting industry."
    )
    if st.button("Contact Me"):
        show_contact_form()


# --- experience ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - simply dummy text of the printing and typesetting industry
    - simply dummy text of the printing and typesetting industry
    - simply dummy text of the printing and typesetting industry
    - simply dummy text of the printing and typesetting industry
    """
)

# --- skills ---
st.write("\n")
st.subheader("My Skills", anchor=False)
st.write(
    """
    - simply dummy text of the printing and typesetting industry
    - simply dummy text of the printing and typesetting industry
    - simply dummy text of the printing and typesetting industry
    - simply dummy text of the printing and typesetting industry
    """
)













