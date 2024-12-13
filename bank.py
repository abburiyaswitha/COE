import streamlit as st
class Bank:
    balance = 10000 
    def deposit(self):
        amount = st.number_input("Enter deposit amount:", min_value=100,max_value=50000,step=100)
        if 100 <= amount <= 50000 and amount % 100 == 0:
            Bank.balance += amount
            st.success(f"Successfully deposited {amount}.New balance:{Bank.balance}")
        else:
            st.error("Invalid deposit amount.")
    def withdraw(self):
        amount = st.number_input("Enter withdrawal amount:", min_value=100, max_value=20000, step=100)
        if 100 <= amount <= 20000 and amount % 100 == 0 and amount <= Bank.balance and (Bank.balance - amount) >= 500:
            Bank.balance -= amount
            st.success(f"Successfully withdraw {amount}. New balance: {Bank.balance}")
        else:
            st.error("Invalid withdrawal.")
    def balance_enquiry(self):
        st.write(f"Current balance:{Bank.balance}")
    def authenticate(self):
        pin = st.text_input("Enter your PIN",type="password")
        if pin == "1234":
            st.success("PIN validated successfully.")
            return True
        else:
            st.error("Invalid PIN!")
            return False
obj = Bank()
if obj.authenticate():
    option = st.radio("Choose an option:", ["Deposit", "Withdraw", "Balance Enquiry"])
    if option == "Deposit":
        obj.deposit()
    elif option == "Withdraw":
        obj.withdraw()
    elif option == "Balance Enquiry":
        obj.balance_enquiry()
