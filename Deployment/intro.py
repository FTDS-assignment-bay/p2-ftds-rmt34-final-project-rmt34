import streamlit as st


def run():
    st.image("images/logo.png")
    st.title("UJATIM - Udang Jawa Timur")
    st.write("---")
    st.markdown("""
    UJATIM atau Udang Jawa Timur merupakan platform inovatif yang didedikasikan untuk memprediksi harga udang vaname di Provinsi Jawa Timur. Platform ini hadir untuk membantu para petani udang vanname dalam memprediksi harga sehingga dapat lebih efisien dalam mengatur pasokan mereka. Dengan demikian, diharapkan dapat memenuhi permintaan dan memaksimalkan keuntungan.
    """)

    st.write("## Visi")
    st.write("""
    Mewujudkan prediksi harga udang vaname yang akurat dan andal untuk mendukung pengambilan keputusan yang lebih baik di seluruh rantai pasokan, meningkatkan efisiensi, dan memaksimalkan keuntungan bagi petani dan pelaku pasar di Provinsi Jawa Timur.
    """)

    st.write("## Misi")
    st.write("""
    - Mengembangkan model prediksi harga udang berbasis analisis time series dengan memanfaatkan data historis.
    - Menyediakan wawasan yang mendalam tentang distribusi dan fluktuasi harga udang vaname di Provinsi Jawa Timur.
    - Memberikan solusi berbasis data yang dapat membantu petani, pedagang, dan pengelola rantai pasokan dalam merencanakan stok dan strategi harga.
    - Mendorong adopsi teknologi untuk meningkatkan efisiensi di sektor perikanan, khususnya bagi petani udang vaname.
    """)

    st.write("## Penyusun")
    st.write("""
    1. Asyam Rafif Rizqullah (Data Engineer)
    2. Dery Rai Ambhara (Data Scientist)
    3. Fahmi Aziz (Data Scientist)
    4. Muhammad Asril Hanif (Data Engineer)
    5. Shinta Amalia (Data Analyst)
             """)


if __name__ == '__main__':
    run()