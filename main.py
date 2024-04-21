import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

st.title('Find the Largest Number')
st.header('Enter three numbers to find the largest among them.')

# Input from the user
number1 = st.number_input('Enter first number:', format='%d')
number2 = st.number_input('Enter second number:', format='%d')
number3 = st.number_input('Enter third number:', format='%d')

if st.button('Find Largest'):
    largest = find_largest(number1, number2, number3)
    st.success(f'The largest number is {largest}')
