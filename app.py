import streamlit as st

st.header("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")
a = st.number_input("Enter the first number:")
#x = st.number_input("Enter the first number:",1,10)
b = st.number_input("Enter the second number:")
op = st.selectbox("Select operator:", ["+", "-", "*", "/", "**", "%"])

submit=st.button('Calculate')


#from cal import fun, mulply, divide, add, subtract, power, mod
from cal import *
result = fun(a, b, op)
st.write("Result:", result)

if submit:
  if op == '+':
      res = add(a, b)
  elif op == '-':
      res = subtract(a, b)
  elif op == '*':
      res = multiply(a, b)
  elif op == '/':
    res = divide(a, b)
  elif op == '%':
    res = mod(a, b)
 
  st.write(f"The Answer is: {res}")          