import streamlit as st
from sources import DEFAULT_BOOKS, search_pdfs, fetch_pdf_text

st.set_page_config(page_title="BTÜ Akıllı Ders Asistanı", page_icon="🎓", layout="wide")

st.title("🎓 BTÜ Endüstri Mühendisliği Akıllı Asistanı")
st.markdown("Ders notlarını arayın, soruları çözdürün ve çalışma materyallerine hızlıca erişin.")

# Sidebar - Ders Seçimi
st.sidebar.header("📚 Ders ve Kaynak Yönetimi")
course_list = list(DEFAULT_BOOKS.keys()) + ["Diğer (Özel Ders)"]
course = st.sidebar.selectbox("Ders Seçin", course_list)

if course == "Diğer (Özel Ders)":
    course_name = st.sidebar.text_input("Ders Adı Girin", "Örn: Tesis Planlama")
else:
    course_name = course

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Önerilen Kaynaklar")
if course in DEFAULT_BOOKS:
    for url in DEFAULT_BOOKS[course]:
        st.sidebar.markdown(f"- [PDF Kaynağını Aç]({url})")

# Ana Ekran Sekmeleri (Interaktif Butonlar ve Alanlar)
tab1, tab2, tab3 = st.tabs(["🔍 Soru & Çözüm Avcısı", "📝 Akıllı Ders Notu", "💡 Formül & Kavramlar"])

with tab1:
    st.subheader("Sorunuzu veya Aradığınız Konuyu Girin")
    query = st.text_input("Örn: Lineer programlama simpleks yöntemi adımları nelerdir?", placeholder="Sorunuzu buraya yazın...")
    
    if st.button("Soru Çöz ve Kaynak Ara", type="primary"):
        if query:
            with st.spinner("Kaynaklar taranıyor ve çözüm üretiliyor..."):
                results = search_pdfs(query)
                st.success("Sonuçlar Başarıyla Bulundu!")
                st.markdown("### 📌 İlgili Kaynaklar:")
                for res in results:
                    st.markdown(f"- **{res['title']}**: [{res['href']}]({res['href']})")
                
                st.markdown("---")
                st.markdown("### 🤖 Yapay Zeka Çözüm Önerisi:")
                st.info(f"'{query}' konusu için Endüstri Mühendisliği perspektifinden analiz: Bu problem matematiksel modelleme, kısıtlar ve amaç fonksiyonu tanımlanarak adım adım çözülür.")
        else:
            st.warning("Lütfen aramak için bir soru veya konu yazın.")

with tab2:
    st.subheader("Otomatik Ders Notu Özeti")
    note_topic = st.text_input("Özetlenmesini istediğiniz konu başlığı:", "Yöneylem Araştırması Temelleri")
    if st.button("Ders Notu Oluştur"):
        st.success(f"'{note_topic}' için özet notlar hazırlandı:")
        st.markdown("""
        * **Ana Tanım:** Sistemlerin optimizasyonu ve verimlilik analizi.
        * **Temel Formülasyon:** Amaç fonksiyonu $\\max Z = c^T x$ kısıtlar altında $Ax \\le b$.
        * **Uygulama Alanları:** Üretim planlama, lojistik, envanter yönetimi.
        """)

with tab3:
    st.subheader("Hızlı Formül ve Kavram Sözlüğü")
    st.markdown("Seçilen ders kapsamında sık kullanılan formüller ve kavramlar:")
    st.markdown("- **Üretim Verimliliği:** Çıktı / Girdi")
    st.markdown("- **Kapasite Kullanım Oranı:** Gerçekleşen Üretim / Toplam Kapasite")
