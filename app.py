import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sosyal Etki Analizörü", page_icon="🌱")
st.title("🌱 Sosyal Etki & Politika Analizörü")

# Yan Panel
api_key = st.sidebar.text_input("Gemini API Key:", type="password")
st.sidebar.info("Google AI Studio'dan aldığınız anahtarı buraya yapıştırıp ENTER'a basın.")

# Ana Ekran
user_input = st.text_area("Analiz edilecek metni buraya yazın:", height=200)

if st.button("Analizi Başlat"):
    if not api_key:
        st.error("Lütfen önce sol tarafa API Key giriniz!")
    elif not user_input:
        st.warning("Lütfen analiz edilecek bir metin girin.")
    else:
        try:
            genai.configure(api_key=api_key)
            # En güncel ve her anahtarla çalışan model ismi:
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner('Analiz ediliyor...'):
                response = model.generate_content(f"Bir siyaset bilimci gözüyle şu metni analiz et: {user_input}")
                st.success("✅ Analiz Tamamlandı!")
                st.write(response.text)
        except Exception as e:
            st.error(f"Hata oluştu: {e}")

st.divider()
st.caption("Feride Ece - İstanbul Üniversitesi")
