import streamlit as st
from Number_to_Words_Converter import convert

st.set_page_config(page_title="Number to Words", layout="centered")

st.title("🔢 Number to Words Converter")

# Input box
user_input = st.text_input("Enter a number (up to 7 digits):")

if user_input:
    if user_input.isdigit():
        if len(user_input) <= 7:
            number = int(user_input)
            words = convert(number)
            st.success(f"🗣️ In words: **{words}**")
        else:
            st.error("Number must be 7 digits or fewer.")
    else:
        st.error("Please enter digits only.")
