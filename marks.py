import streamlit as st
st.title("Grade Calculation")
project = st.number_input("Enter project marks:", min_value=0, max_value=100)
internal = st.number_input("Enter internal marks:", min_value=0, max_value=100)
external = st.number_input("Enter external marks:", min_value=0, max_value=100)
if project > 50 and internal > 50 and external > 50:
    total_marks = (70 / 100) * project + (10 / 100) * internal + (20 / 100) * external
    if total_marks > 90:
        st.write("Grade:A")
    elif 80 < total_marks <= 90:
        st.write("Grade:B")
    else:
        st.write("Grade:C")
else:
    if project < 50:
        st.write("Failed in project")
    if internal < 50:
        st.write("Failed in internal")
    if external < 50:
        st.write("Failed in external")
