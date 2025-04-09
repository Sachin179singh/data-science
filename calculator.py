import streamlit as st

st.title("Simple Calculator")
st.write("This is a simple calculator app using streamlit.")      # write or markdown

fnum = st.number_input("First Number", value=0) 
snum = st.number_input("Second Number", value=0)  