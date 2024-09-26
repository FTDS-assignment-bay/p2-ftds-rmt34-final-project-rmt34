'''
Import Library
'''
import streamlit as st
import pandas as pd
import pickle

def run():
    '''
    Load Model
    '''
    with open('model30.pkl','rb') as model30_file:
        model30 = pickle.load(model30_file)
    with open('model40.pkl','rb') as model40_file:
        model40 = pickle.load(model40_file)
    with open('model50.pkl','rb') as model50_file:
        model50 = pickle.load(model50_file)
    with open('model60.pkl','rb') as model60_file:
        model60 = pickle.load(model60_file)
    with open('model70.pkl','rb') as model70_file:
        model70 = pickle.load(model70_file)
    with open('model80.pkl','rb') as model80_file:
        model80 = pickle.load(model80_file)
    with open('model100.pkl','rb') as model100_file:
        model100 = pickle.load(model100_file)

    '''
    Load Datasets
    '''
    df = pd.read_csv("shrimp_prices_week.csv")

    df['date']=pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    '''
    Page Title
    '''
    st.write("## Harga Udang di Jawa Timur 4 minggu terakhir : ")
    st.dataframe(df.tail(4))

    st.write("## Prediksi Harga Udang")
    '''
    Dictionary untuk menyimpan ukuran udang dan modelnya
    '''
    model_dict = {
        '30':model30,
        '40':model40,
        '50':model50,
        '60':model60,
        '70':model70,
        '80':model80,
        '100':model100
    }
    size_select = st.selectbox('Size Udang :', ('30','40','50','60','70','80','100'), index=0)
    date_to_predict = st.date_input('Tanggal Jual :')
    model = model_dict[size_select]

    pred = model.predict(start="2024-09-23", end=date_to_predict)
    pred = pd.DataFrame(pred)
    pred.columns=['Price Prediction']

    st.dataframe(pred.tail(2))


if __name__ == '__main__':
    run()