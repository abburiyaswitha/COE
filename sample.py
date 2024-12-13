import streamlit as st
st.title("Even OR Odd")
num1 = st.number_input("Enter number", min_value=1,step=1)
if st.button("enev/odd"):
    if num1%2==0:
        st.success("even number")
    else:
        st.error("odd")