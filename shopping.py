import streamlit as st
st.title("Shopping Bill")
salary = st.number_input("Enter the employee's salary:", min_value=0)
bill1 = st.number_input("Enter the first shopping bill amount:", min_value=0)
bill2 = st.number_input("Enter the second shopping bill amount:", min_value=0)
bill3 = st.number_input("Enter the third shopping bill amount:", min_value=0)
total_shopping_amount = bill1 + bill2 + bill3
if salary > 0:
    percentage_spent = (total_shopping_amount * 100)/salary
    st.write(f"Total shopping amount: {total_shopping_amount}")
    st.write(f"The percentage of salary spent on shopping: {percentage_spent:2f}%")
else:
    st.error("Salary must be greater than 0 to calculate percentage spent.")
