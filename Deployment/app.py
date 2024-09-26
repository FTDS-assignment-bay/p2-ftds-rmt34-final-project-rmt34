import streamlit as st
import intro
import eda
import prediction

st.set_page_config(
    page_title='UJATIM - Udang Jawa Timur',
    layout='wide',
    initial_sidebar_state='expanded'
)

page = st.sidebar.selectbox('Pilih Halaman', ('Home','Eksplorasi Harga Udang','Prediksi Harga Mendatang'))

if page == 'Home':
    intro.run()
elif page == 'Eksplorasi Harga Udang':
    eda.run()
else:
    prediction.run()

