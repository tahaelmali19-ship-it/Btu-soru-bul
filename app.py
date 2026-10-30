import streamlit as st
from sources import BTU_DATABASE

st.set_page_config(page_title="BTU Akıllı Akademik Asistan", page_icon="🎓", layout="wide")

st.title("🎓 BTU Akademik Ders ve Soru Bankası Asistanı")
st.markdown("Bölüm, sınıf, ders ve konu seçerek üniversite kaynaklı tüm sorulara ve çözümlere ulaşın.")

# Hiyerarşik Sidebar Menü (Bölüm -> Sınıf -> Ders -> Bölüm/Konu)
st.sidebar.header("🧭 Akademik Filtreleme")

# 1. Bölüm Seçimi
bolum_listesi = list(BTU_DATABASE.keys())
secilen_bolum = st.sidebar.selectbox("1️⃣ Bölüm Seçin", bolum_listesi)

# 2. Sınıf Seçimi
sinif_listesi = list(BTU_DATABASE[secilen_bolum].keys())
secilen_sinif = st.sidebar.selectbox("2️⃣ Sınıf Seçin", sinif_listesi)

# 3. Ders Seçimi
ders_listesi = list(BTU_DATABASE[secilen_bolum][secilen_sinif].keys())
secilen_ders = st.sidebar.selectbox("3️⃣ Ders Seçin", ders_listesi)

# Ders detaylarını al
ders_bilgi = BTU_DATABASE[secilen_bolum][secilen_sinif][secilen_ders]

# 4. Konu / Bölüm Seçimi (Örn: Limit ve Süreklilik)
konu_listesi = list(ders_bilgi["bolumler"].keys())
secilen_konu = st.sidebar.selectbox("4️⃣ Kitap / Konu Bölümü Seçin", konu_listesi)

st.sidebar.markdown("---")
st.sidebar.subheader("📖 Üniversite Ana Kaynağı")
st.sidebar.markdown(f"**{ders_bilgi['ana_kaynak']}**")
st.sidebar.markdown(f"[🔗 Kaynak PDF / Sayfaya Git]({ders_bilgi['kaynak_url']})")

# Ana Ekran
st.header(f"📚 {secilen_ders} — {secilen_konu}")
st.markdown(f"**Seçilen Bölüm:** {secilen_bolum} | **Sınıf:** {secilen_sinif}")

st.markdown("---")
st.subheader("📝 Seçilen Konuya Ait Tüm Sorular ve Çözümleri")

# Seçilen konudaki tüm soruları listele
sorular = ders_bilgi["bolumler"][secilen_konu]

for i, soru_obj in enumerate(sorular, 1):
    with st.expander(f"Soru {i}: {soru_obj['soru'][:50]}...", expanded=True):
        st.markdown(f"### ❓ Soru {i}:")
        st.write(soru_obj['soru'])
        
        st.markdown(f"### ✅ Çözüm:")
        st.success(soru_obj['cozum'])
        
        st.markdown(f"### 📌 Kaynak Bilgisi:")
        st.info(f"Bu soru ve çözüm **{soru_obj['kaynak_detay']}** kaynağından alınmıştır.")

st.markdown("---")
if st.button("🤖 Yapay Zeka ile Bu Konuyu Özetle"):
    st.info(f"**{secilen_konu}** konusu, Endüstri Mühendisliği ve temel mühendislik uygulamalarında problem çözme becerilerinin temelini oluşturur. Yukarıdaki kaynak soruları inceleyerek benzer problem tiplerini çözebilirsiniz.")
