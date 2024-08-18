import streamlit as st

# --- page setup ---

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:",
)


# --- navigation setup [without sections]---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- navigation setup [with sections]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- shared on all pages ---
st.logo("assets/images/logo.png")
st.sidebar.text("Made with Love by Freetime..")


# --- run navigation ---
pg.run()


