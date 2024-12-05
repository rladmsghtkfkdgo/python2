import streamlit as st
st.title('st.form')
st.header('1.with 표기법 사용 예시')
st.subheader('coffee machine')
with st.form('my_form'):
    st.subheader('===order coffee===')
    coffee_bean=st.selectbox('coffee bean', ['arabica','robstar'])
    coffee_roast=st.selectbox('coffee roasting', ['light','mideum','dark'])
    brewing=st.selectbox('brewing',['airopress','drip','frenchpress','mochapoto','syphone'])
    serving=st.selectbox('serving',['hot','ice','frape'])
    milk=st.select_slider('milk',['none','low','mideum','high'])
    owncup=st.checkbox('Do you have your own cup?')
    submitted=st.form_submit_button('submit')
    
if submitted:
    st.markdown(f'''
        ===your order===\n
        -coffee bean:'{coffee_bean}'
        -coffee roastring:'{coffee_roast}'
        -brewing:'{brewing}'
        -serving:'{serving}'
        -milk:'{milk}'
        -own cup:'{owncup}'
        ''')
else:
    st.write('make order please')
        

