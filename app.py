import streamlit as st
from sources import DEFAULT_BOOKS, search_pdfs

st.set_page_config(page_title="BTÜ Akıllı Ders Asistanı", page_icon="🎓", layout="wide")

st.title("🎓 BTÜ Endüstri Mühendisliği Akıllı Asistanı")
st.markdown("Ders bazlı kategoriler, üniversite kaynakları ve akıllı soru çözüm sistemi.")

# Sidebar - Ders ve Kategori Seçimi
st.sidebar.header("📚 Ders ve Kategori Filtresi")
course_names = list(DEFAULT_BOOKS.keys())
selected_course = st.sidebar.selectbox("Ders Seçin", course_names)

# Seçilen dersin alt kategorilerini al
categories = DEFAULT_BOOKS[selected_course]["kategoriler"]
selected_category = st.sidebar.selectbox("Soru / Konu Kategorisi", categories)

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Üniversitenin Önerdiği Kaynaklar")
for kaynak in DEFAULT_BOOKS[selected_course]["kaynaklar"]:
    st.sidebar.markdown(f"- [{kaynak['title']}]({kaynak['href']})")

# Ana Ekran Sekmeleri
tab1, tab2, tab3 = st.tabs(["🔍 Soru Çöz & Kaynak Eşleştir", "📝 Akıllı Ders Notu", "💡 Formül & Özet"])

with tab1:
    st.subheader(f"Ders: {selected_course} | Kategori: {selected_category}")
    query = st.text_input("Çözülmesini istediğiniz soruyu veya konuyu yazın:", placeholder="Örn: Bu kategorideki optimal çözüm adımları nelerdir?")
    
    if st.button("Soruyu Çöz ve Kaynağı Göster", type="primary"):
        if query:
            with st.spinner("Üniversite kaynakları taranıyor ve çözüm üretiliyor..."):
                kaynaklar = search_pdfs(selected_course, selected_category, query)
                
                st.success("Çözüm ve Kaynak Eşleştirmesi Tamamlandı!")
                
                st.markdown("### 📌 Bu Bilginin Alındığı Üniversite Kaynağı:")
                # Kullanıcıya sorunun hangi kaynaktan alındığını net şekilde gösteriyoruz
                st.info(f"📚 **Kaynak Adı:** {kaynaklar[0]['title']}\n🔗 **Bağlantı:** [Kaynağa Git]({kaynaklar[0]['href']})")
                
                st.markdown("### 🤖 Yapay Zeka Çözüm ve Analiz Önerisi:")
                st.markdown(f"""
                * **Seçilen Kategori:** {selected_category}
                * **Soru/Konu:** {query}
                * **Çözüm Adımları:** 
                  1. Verilen kısıtlar ve parametreler üniversite kaynak standardına göre modellenir.
                  2. İlgili formül uygulanarak matematiksel çözüm türetilir.
                  3. Çıkan sonuç Endüstri Mühendisliği perspektifinden yorumlanır.
                """)
        else:
            st.warning("Lütfen bir soru veya konu girin.")

with tab2:
    st.subheader(f"{selected_course} - {selected_category} Ders Notları")
    st.markdown(f"**{selected_selected = selected_category}** odaklı otomatik ders özeti ve önemli ipuçları bu alanda yer almaktadır.")
    st.markdown("- Üniversite müfredatına uyumlu konu anlatımı.")
    st.markdown("- Sınavlarda çıkabilecek soru kalıpları.")

with tab3:
    st.subheader("Hızlı Formül ve Kavramlar")
    st.markdown(f"**{selected_course}** dersi için bu kategoride bilmeniz gereken temel formüller.")
