import streamlit as st
st.title('a small program')
st.subheader('I am Suu Wai Moe')
st.write('Multiplication table')
num = int(input('Please enter a number:'))
for i in range(1,13):
    result = i * num
    print(num ,' X ', i , ' => ' , result)
    
