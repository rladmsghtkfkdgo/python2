import streamlit as st

st.header('st.selectbox')

option =st.selectbox(
    'whats your favorite color?',
    ('blue','red','green')
)
st.write('your favorite color is', option)