import streamlit as st 

# 设置全局属性
st.set_page_config(
    page_title='我是标题',
    page_icon=' ',
    layout='wide'
)
c1, c2 = st.columns(spec=2)

# 将被渲染在最下方
st.title('hello')
st.write('this is a simple python code')
with st.echo():
    foo_dict = { i : i for i in range(10)}
    
with c2:
    st.title('column Ⅱ')
    st.info('content in column Ⅱ')

with c1:
    st.title('column Ⅰ')
    c_1_1, c_1_2 = c1.columns(spec=2)

    with c_1_1:
        st.info('sub column 1 in column Ⅰ')

    with c_1_2:
        st.info('sub column 2 in column Ⅱ')
