import streamlit as st
import re

st.set_page_config(page_title=" Password Strength Checker", page_icon="🔐")
# Sidebar Theme Toggle
theme = st.sidebar.radio("Select Theme:", ["Light Mode", "Dark Mode"])

# Custom Styling
if theme == "Dark Mode":
    st.markdown(
        """
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stTextInput>div>div>input { background-color: #333; color: white; }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("🔐  Password Strength Checker")
password = st.text_input("Enter a Password", type="password")
feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌password shoud be a latest 8 character long.")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else :
        feedback.append("🔠 Include both uppercase and lowercase letters.")
    if re.search(r'\d', password):
       score += 1
    else :
        feedback.append("🔢 Include at least one number (0-9).")

    if re.search(r'[!@#$&%]',password):
        score += 1
    else :
        feedback.append("🔣 Include at least one special character (!@#$&%).")
    if score == 4:
        feedback.append("✅Your password is strong! 💪")
        st.balloons()
    elif score == 3:
        feedback.append("🟡Your password is mediam strength. It could be stronger")
    else :
        feedback.append("🔴Your password is weak . please make it stonger")

    if feedback:
        st.markdown("## Improvement Suggestions: ")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please Enter your password to get started")
    

