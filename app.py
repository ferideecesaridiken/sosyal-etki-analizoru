import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sosyal Etki Analizörü", page_icon="🌱")

st.title("🌱 Sosyal Etki & Politika Analizörü")
st.markdown("YGA & Up School - Future Talent Programı Bitirme Projesi")

with st.sidebar:
    st.header("⚙️ Ayarlar")
    api_key = st.text_input("Gemini API Key:", type="password")
    st.info("API Key'inizi Google AI Studio'dan alabilirsiniz.")

user_input = st.text_area("Analiz edilecek metni buraya yazın:", height=200)

if st.button("Analizi Başlat"):
    if not api_key:
        st.error("Lütfen önce API Key giriniz!")
    elif not user_input:
        st.warning("Lütfen bir metin giriniz.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # BURASI KRİTİK: Önce Flash modelini deniyoruz, olmazsa Pro modeline geçiyoruz
            with st.spinner('Yapay zeka analiz ediyor...'):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"Bir siyaset bilimci gözüyle şu metnin sosyal etkisini ve BM hedefleriyle uyumunu analiz et: {user_input}"
                    response = model.generate_content(prompt)
                except:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(prompt)
                
                st.success("✅ Analiz Tamamlandı!")
                st.write(response.text)
        except Exception as e:
            st.error(f"Sistemde bir sorun oluştu. Lütfen API anahtarınızı kontrol edin.")
            st.info(f"Hata detayı: {e}")

st.divider()
st.caption("Feride Ece - İstanbul Üniversitesi Siyaset Bilimi ve Uluslararası İlişkiler")
