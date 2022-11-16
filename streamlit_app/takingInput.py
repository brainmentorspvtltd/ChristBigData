import streamlit as st

st.title("Streamlit Taking Input Example")
st.write("Simple Example to take input from user...")

form = st.form(key = "my_form")
name = form.text_input(label="Enter your name : ")
age = form.text_input(label="Enter your age : ")

submit = form.form_submit_button(label="Say Hello...")

if submit:
    st.write("Hello {}".format(name))
    st.write("Age is {}".format(age))

