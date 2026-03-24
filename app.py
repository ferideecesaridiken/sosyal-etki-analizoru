import streamlit as st
import google.generativeai as genai

# Sayfa tasarımı
st.set_page_config(page_title="Sosyal Etki Analizörü", page_icon="🌱")

st.title("🌱 Sosyal Etki & Politika Analizörü")
st.markdown("YGA & Up School - Future Talent Programı Bitirme Projesi")

# Sol Panel
with st.sidebar:
    st.header("⚙️ Ayarlar")
    api_key = st.text_input("Gemini API Key giriniz:", type="password")
    st.info("API Key'inizi Google AI Studio'dan alabilirsiniz.")

# Ana Ekran
user_input = st.text_area("Analiz edilecek metni buraya yapıştırın:", height=200)

if st.button("Analizi Başlat"):
    if not api_key:
        st.error("Lütfen önce sol tarafa API Key giriniz!")
    elif not user_input:
        st.warning("Lütfen analiz edilecek bir metin girin.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # 2026'nın asıl modeli: gemini-3-flash
            model = genai.GenerativeModel('gemini-3-flash')
            
            with st.spinner('Yapay zeka analiz ediyor...'):
                prompt = f"Bir siyaset bilimci gözüyle şu metni analiz et ve sosyal etkisini, BM hedefleriyle uyumunu ve iyileştirme önerilerini maddeler halinde yaz: {user_input}"
                response = model.generate_content(prompt)
                
                st.success("✅ Analiz Tamamlandı!")
                st.markdown("### 📊 Analiz Sonuçları")
                st.write(response.text)
        except Exception as e:
            # Hata olursa model ismini otomatik düzeltmeyi dener
            st.error("Bir bağlantı sorunu oluştu, sistem güncelleniyor...")
            try:
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content(prompt)
                st.success("✅ Analiz Tamamlandı!")
                st.write(response.text)
            except:
                st.info("Lütfen API anahtarınızın aktif olduğunu kontrol edin.")

st.divider()
st.caption("Feride Ece - İstanbul Üniversitesi Siyaset Bilimi ve Uluslararası İlişkiler")
