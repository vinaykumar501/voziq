import streamlit as st
st.header("EMI Calculator")
amount=st.number_input("enter the amount:")
rate=st.number_input("enter the rate of interest:")
time=st.number_input("enter the time:")
emi=amount*time*rate/100


calulate=st.button('Calculate')
if calulate:
 st.write(f"The EMI is: {emi}")
