import streamlit as st
import pandas as pd

def run():
    '''
    Title
    '''
    st.write('# UJATIM - Udang Jawa Timur')
    st.write("---")

    '''
    Load Datasets
    '''
    df = pd.read_csv("shrimp_prices_week.csv")

    df['date']=pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    df_2 = df.rename(columns={'size_30':'size_030','size_40':'size_040','size_50':'size_050','size_60':'size_060','size_70':'size_070','size_80':'size_080','size_100':'size_100'})
    df_stat = df_2.describe().T
    '''
    Plot Trend Harga Udang
    '''
    st.write("## Trend Harga Udang")
    st.write("---")
    st.line_chart(df)

    st.write("""
    Berdasarkan plot diatas dapat dilihat bahwa:
    1. Harga udang vaname secara berurutan dari tinggi kerendah yaitu size 30, size 40, size 50, size 60, size 70, size 80, dan size 100.
    2. Tren harga udang pada setiap size cenderung tidak memiliki perbedaan yang signifikan dan cenderung merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
    3. Penurunan harga udang vaname terjadi di sekitar kuartal ke 2/4 tahun 2019 dan 2020 serta kuartal 4/4 tahun 2022 dan 2023, dengan detail sebagai berikut:
        - Untuk tahun 2019 kemungkinan penurunan terjadi pengurangan permintaan khususnya dari luar negeri dikarenakan stok yang mereka punya sudah penuh. (1)
        - Untuk tahun 2020 kemungkinan penurunan terjadi karena adanya pandemi covid-19 yang melanda Indonesia sehingga berpengaruh terhadap permintaan. (2)
        - Untuk tahun 2022 dan 2023 kemungkinan penurunan terjadi karena adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (3)
    Sumber:

    (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot

    (2). https://jala.tech/id/blog/tips-budidaya/tren-harga-udang-2020-bagaimana-2021

    (3). https://www.liputan6.com/amp/5546128/harga-udang-naik-turun-ekstrem-petambak-diminta-lakukan-ini


    """)
    '''
    Harga Rata-rata Udang per Ukuran
    '''
    st.write("## Harga Rata-rata Udang per Ukuran")
    st.write("---")
    st.bar_chart(df_stat['mean'], x_label='Ukuran Udang', y_label='Rata-rata Harga (Rupiah)')
    st.write("""
    Dari grafik diatas terlihat semakin kecil kategori size nya maka semakin tinggi harganya. Hal itu dikarenakan "Size" pada data ini bukan ukuran 1 ekor udang, melainkan diterjemahkan sebagai jumlah ekor udang per 1Kg-nya. Sehingga semakin sedikit jumlah udang per Kg-nya maka semakin besar ukuran udang per ekornya dan semakin tinggi pula harganya.
             """)
    
    st.write("## Pilih Size Udang :")
    option = st.selectbox('Size :', ('30','40','50','60','70','80','100'), index=0)

    if option == '30':
        '''
        Harga Size 30
        '''
        st.write("## Harga Udang Size 30")
        st.write("---")
        st.line_chart(df['size_30'])
        st.write("""
        Dari plot tren diatas dapat diketahui bahwa:
        1. Data untuk size 30 merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
        2. Terjadi penurunan yang cukup anjlok pada akhir tahun 2022 dan 2023 yang mana disebabkan oleh adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (1)

        Sumber:

        (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot
        """)
        
        st.write("### Rata-rata, Median, Minimum, dan Maksimum Harga")
        st.write("---")
        hitungan(df['size_30'])
        st.image("images/size_30_distri.png")

    elif option == "40":
        '''
        Harga Size 40
        '''
        st.write("## Harga Udang Size 40")
        st.write("---")
        st.line_chart(df['size_40'])
        st.write("""
        Dari plot tren diatas dapat diketahui bahwa:
        1. Data untuk size 40 merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
        2. Terjadi penurunan yang cukup anjlok pada akhir tahun 2022 dan 2023 yang mana disebabkan oleh adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (1)

        Sumber:

        (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot""")

        st.write("### Rata-rata, Median, Minimum, dan Maksimum Harga")
        st.write("---")
        hitungan(df['size_40'])
        st.image("images/size_40_distri.png")

    elif option == "50":
        '''
        Harga Size 50
        '''
        st.write("## Harga Udang Size 50")
        st.write("---")
        st.line_chart(df['size_50'])
        st.write("""
        Dari plot tren diatas dapat diketahui bahwa:
        1. Data untuk size 50 merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
        2. Terjadi penurunan pada kuartal 2/4 tahun 2019 kemungkinan diakibatkan dari pengurangan permintaan khususnya dari luar negeri dikarenakan stok yang mereka punya sudah penuh. (1)
        3. Terjadi penurunan pada kuartal 2/4 tahun 2020 kemungkinan diakibatkan dari adanya pandemi covid-19 yang melanda Indonesia sehingga berpengaruh terhadap permintaan. (2)
        4. Terjadi penurunan yang cukup anjlok pada akhir tahun 2022 dan 2023 yang mana disebabkan oleh adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (3)

        Sumber:

        (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot

        (2). https://jala.tech/id/blog/tips-budidaya/tren-harga-udang-2020-bagaimana-2021

        (3). https://www.liputan6.com/amp/5546128/harga-udang-naik-turun-ekstrem-petambak-diminta-lakukan-ini
                 """)
        
        st.write("### Rata-rata, Median, Minimum, dan Maksimum Harga")
        st.write("---")
        hitungan(df['size_50'])
        st.image("images/size_50_distri.png")

    elif option == "60":
        '''
        Harga Size 60
        '''
        st.write("## Harga Udang Size 60")
        st.write("---")
        st.line_chart(df['size_60'])
        st.write("""
        Dari plot tren diatas dapat diketahui bahwa:
        1. Data untuk size 50 merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
        2. Terjadi penurunan pada kuartal 2/4 tahun 2019 kemungkinan diakibatkan dari pengurangan permintaan khususnya dari luar negeri dikarenakan stok yang mereka punya sudah penuh. (1)
        3. Terjadi penurunan pada kuartal 2/4 tahun 2020 kemungkinan diakibatkan dari adanya pandemi covid-19 yang melanda Indonesia sehingga berpengaruh terhadap permintaan. (2)
        4. Terjadi penurunan yang cukup anjlok pada akhir tahun 2022 dan 2023 yang mana disebabkan oleh adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (3)

        Sumber:

        (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot

        (2). https://jala.tech/id/blog/tips-budidaya/tren-harga-udang-2020-bagaimana-2021

        (3). https://www.liputan6.com/amp/5546128/harga-udang-naik-turun-ekstrem-petambak-diminta-lakukan-ini
                """)

        st.write("### Rata-rata, Median, Minimum, dan Maksimum Harga")
        st.write("---")
        hitungan(df['size_60'])
        st.image("images/size_60_distri.png")
    
    elif option == "70":
        '''
        Harga Size 70
        '''
        st.write("## Harga Udang Size 70")
        st.write("---")
        st.line_chart(df['size_70'])
        st.write("""
        Dari plot tren diatas dapat diketahui bahwa:
        1. Data untuk size 70 merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
        2. Terjadi penurunan pada kuartal 2/4 tahun 2019 kemungkinan diakibatkan dari pengurangan permintaan khususnya dari luar negeri dikarenakan stok yang mereka punya sudah penuh. (1)
        3. Terjadi penurunan pada kuartal 2/4 tahun 2020 kemungkinan diakibatkan dari adanya pandemi covid-19 yang melanda Indonesia sehingga berpengaruh terhadap permintaan. (2)
        4. Terjadi penurunan yang cukup anjlok pada akhir tahun 2022 dan 2023 yang mana disebabkan oleh adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (3)

        Sumber:

        (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot

        (2). https://jala.tech/id/blog/tips-budidaya/tren-harga-udang-2020-bagaimana-2021

        (3). https://www.liputan6.com/amp/5546128/harga-udang-naik-turun-ekstrem-petambak-diminta-lakukan-ini
                """)

        st.write("### Rata-rata, Median, Minimum, dan Maksimum Harga")
        st.write("---")
        hitungan(df['size_70'])
        st.image("images/size_70_distri.png")
    
    elif option == "80":
        '''
        Harga Size 80
        '''
        st.write("## Harga Udang Size 80")
        st.write("---")
        st.line_chart(df['size_80'])
        st.write("""
        Dari plot tren diatas dapat diketahui bahwa:
        1. Data untuk size 80 merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
        2. Terjadi penurunan pada kuartal 2/4 tahun 2019 kemungkinan diakibatkan dari pengurangan permintaan khususnya dari luar negeri dikarenakan stok yang mereka punya sudah penuh. (1)
        3. Terjadi penurunan pada kuartal 2/4 tahun 2020 kemungkinan diakibatkan dari adanya pandemi covid-19 yang melanda Indonesia sehingga berpengaruh terhadap permintaan. (2)
        4. Terjadi penurunan yang cukup anjlok pada akhir tahun 2022 dan 2023 yang mana disebabkan oleh adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (3)

        Sumber:

        (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot

        (2). https://jala.tech/id/blog/tips-budidaya/tren-harga-udang-2020-bagaimana-2021

        (3). https://www.liputan6.com/amp/5546128/harga-udang-naik-turun-ekstrem-petambak-diminta-lakukan-ini
                 """)

        st.write("### Rata-rata, Median, Minimum, dan Maksimum Harga")
        st.write("---")
        hitungan(df['size_80'])
        st.image("images/size_80_distri.png")
    
    else:
        '''
        Harga Size 100
        '''
        st.write("## Harga Udang Size 100")
        st.write("---")
        st.line_chart(df['size_100'])
        st.write("""
        Dari plot tren diatas dapat diketahui bahwa:
        1. Data untuk size 100 merupakan **Multiplicative Model** karena data tersebut memiliki lebar & tinggi puncak yang tidak beraturan atau musiman (meningkat/menurun).
        2. Terjadi penurunan pada kuartal 2/4 tahun 2019 kemungkinan diakibatkan dari pengurangan permintaan khususnya dari luar negeri dikarenakan stok yang mereka punya sudah penuh. (1)
        3. Terjadi penurunan pada kuartal 2/4 tahun 2020 kemungkinan diakibatkan dari adanya pandemi covid-19 yang melanda Indonesia sehingga berpengaruh terhadap permintaan. (2)
        4. Terjadi penurunan yang cukup anjlok pada akhir tahun 2022 dan 2023 yang mana disebabkan oleh adanya kelebihan pasokan udang di pasar global serta persaingan yang meningkat dari negara-negara seperti Ekuador dan China. (3)

        Sumber:

        (1). http://trobosaqua.com/detail-berita/2019/10/10/57/12131/menelisik-sebab-harga-udang-merosot

        (2). https://jala.tech/id/blog/tips-budidaya/tren-harga-udang-2020-bagaimana-2021

        (3). https://www.liputan6.com/amp/5546128/harga-udang-naik-turun-ekstrem-petambak-diminta-lakukan-ini
                 """)

        st.write("### Rata-rata, Median, Minimum, dan Maksimum Harga")
        st.write("---")
        hitungan(df['size_100'])
        st.image("images/size_100_distri.png")


def hitungan(data):
    data_stat = pd.DataFrame()
    data_stat.insert(0, "Rata-rata", [data.mean()])
    data_stat.insert(1, "Median", [data.median()])
    data_stat.insert(2, "Minimum", [data.min()])
    data_stat.insert(3, "Maksimum", [data.max()])
    st.dataframe(data_stat)

if __name__ == '__main__':
    run()