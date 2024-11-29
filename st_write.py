import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.write("hello streamlit ...")

#

st.header('Hello, *Wolrd* :sunglasses')

#

st.write(1234)

#

df = pd.DataFrame({
    '첫번째 컬럼':[1,2,3,4],
    '두번째 컬럼':[10,20,30,40]
})
st.write(df)

st.write('아래는 DataFrame입니다.',df,'위는 dataframe입니다.')

df2=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])
c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c'])
st.write(c)
# cmd가서 pip install streamlit 
# 하고 나서 주소찾고 streamlit run 파일명