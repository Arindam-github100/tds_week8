
import streamlit as st
import numpy as np

st.header("Number Adder App")

num1 = st.text_input(label="Enter 1st number")
num2 = st.text_input(label="Enter 2nd number")
btn = st.button("ADD", key="sum")

if btn:
    sum = float(num1) + float(num2)

    st.header(f"""SUM = {sum}""")




