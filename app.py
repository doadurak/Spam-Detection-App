import streamlit as st
import joblib
import numpy as np


model = joblib.load("eniyi.joblib")


st.title("Spam Tespit Web Uygulaması")
st.write("Bu uygulama, e-postaların spam olup olmadığını tahmin etmek için geliştirilmiştir.")


st.header("E-posta Özelliklerini Girin:")
word_count = st.number_input("Kelime Sayısı", min_value=0, step=1)
special_char_count = st.number_input("Özel Karakter Sayısı", min_value=0, step=1)
contains_link = st.selectbox("Link İçeriyor mu?", [0, 1], format_func=lambda x: "Evet" if x == 1 else "Hayır")
spam_words_count = st.number_input("Spam Kelime Sayısı", min_value=0, step=1)


if st.button("Tahmin Et"):
    
    input_data = np.array([[word_count, special_char_count, contains_link, spam_words_count]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Tahmin: Spam")
    else:
        st.success("Tahmin: Spam Değil")

