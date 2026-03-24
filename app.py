import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sosyal Etki Analizörü", page_icon="🌱")
st.title("🌱 Sosyal Etki & Politika Analizörü")

# Yan Panel
api_key = st.sidebar.text_input("Gemini API Key:", type="password")
st.sidebar.info("API Key'i yapıştırıp ENTER'a basın.")

user_input = st.text_area("Analiz edilecek metni buraya yazın:", height=200)

if st.button("Analizi Başlat"):
    if not api_key:
        st.error("Lütfen önce sol tarafa API Key giriniz!")
    elif not user_input:
        st.warning("Lütfen bir metin girin.")
    else:
        try:
            genai.configure(api_key=api_key)
            # 2026'nın asıl modeli:
            model = genai.GenerativeModel('gemini-3-flash')
            
            with st.spinner('Analiz ediliyor...'):
                response = model.generate_content(f"Bir siyaset bilimci olarak şu metni sosyal etkisi ve BM hedefleri açısından analiz et: {user_input}")
                st.success("✅ Analiz Tamamlandı!")
                st.write(response.text)
        except Exception as e:
            st.error(f"Bağlantı hatası: {e}")

st.divider()
st.caption("Feride Ece - İstanbul Üniversitesi")
