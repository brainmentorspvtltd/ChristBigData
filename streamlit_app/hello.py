import streamlit as st

val = st.slider("val")
st.write(val, "squared is",val * val)

# open new terminal
# type - streamlit run file_name.py