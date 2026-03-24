import streamlit as st
import google.generativeai as genai

# Sayfa ayarları
st.set_page_config(page_title="Sosyal Etki Analizörü", page_icon="🌱")

# Stil ve başlık
st.title("🌱 Sosyal Etki & Politika Analizörü")
st.markdown("""
Bu araç, metinleri **sosyal fayda**, **politik ton** ve **Sürdürülebilir Kalkınma Amaçları** açısından analiz eder. 
*YGA & Up School - Future Talent Programı için geliştirilmiştir.*
""")

# Yan menüde API girişi
with st.sidebar:
    st.header("⚙️ Yapılandırma")
    api_key = st.text_input("Gemini API Key giriniz:", type="password")
    st.info("API Key'inizi Google AI Studio'dan alabilirsiniz.")

# Ana ekran
user_input = st.text_area("Analiz edilecek metni buraya yapıştırın (Haber, yasa tasarısı, proje taslağı vb.):", height=200)

if st.button("Analizi Başlat"):
    if not api_key:
        st.error("Lütfen önce sol tarafa API Key giriniz!")
    elif not user_input:
        st.warning("Lütfen analiz edilecek bir metin girin.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            with st.spinner('Yapay zeka analiz ediyor...'):
                prompt = f"""
                Bir siyaset bilimci ve sosyal girişimci gözüyle şu metni analiz et:
                '{user_input}'
                
                Lütfen şu başlıklarla yanıt ver:
                1. Sosyal Fayda Puanı (10 üzerinden) ve nedeni.
                2. BM Sürdürülebilir Kalkınma Amaçları ile uyumu (Hangi maddeler?).
                3. Politik Ton ve Tarafsızlık Analizi.
                4. Bu çalışmayı daha 'toplum yararına' hale getirmek için 3 öneri.
                """
                response = model.generate_content(prompt)
                
                st.success("✅ Analiz Tamamlandı!")
                st.markdown("### 📊 Analiz Sonuçları")
                st.write(response.text)
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")

st.divider()
st.caption("Feride Ece - Siyaset Bilimi ve Uluslararası İlişkiler Öğrencisi tarafından hazırlanmıştır.")
