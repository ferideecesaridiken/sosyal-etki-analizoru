import streamlit as st
import google.generativeai as genai

# Sayfa tasarımı
st.set_page_config(page_title="Sosyal Etki Analizörü", page_icon="🌱")

st.title("🌱 Sosyal Etki & Politika Analizörü")
st.markdown("YGA & Up School - Future Talent Programı Bitirme Projesi")

# Sol Panel
with st.sidebar:
    st.header("⚙️ Ayarlar")
    api_key = st.text_input("Gemini API Key:", type="password")
    st.info("API Key'inizi Google AI Studio'dan alabilirsiniz.")

# Ana Ekran
user_input = st.text_area("Analiz edilecek metni buraya yazın:", height=200)

if st.button("Analizi Başlat"):
    if not api_key:
        st.error("Lütfen önce API Key giriniz!")
    elif not user_input:
        st.warning("Lütfen bir metin giriniz.")
    else:
        try:
            genai.configure(api_key=api_key)
            # En güncel ve hızlı model ismini kullanıyoruz
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner('Yapay zeka analiz ediyor, lütfen bekleyin...'):
                prompt = f"Bir siyaset bilimci gözüyle şu metni analiz et ve sosyal etkisini, BM hedefleriyle uyumunu ve iyileştirme önerilerini maddeler halinde yaz: {user_input}"
                response = model.generate_content(prompt)
                
                st.success("✅ Analiz Tamamlandı!")
                st.write(response.text)
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
            st.info("İpucu: API anahtarınızın doğru olduğundan ve Google AI Studio'da Gemini API'nin etkin olduğundan emin olun.")

st.divider()
st.caption("Feride Ece - İstanbul Üniversitesi Siyaset Bilimi ve Uluslararası İlişkiler")
