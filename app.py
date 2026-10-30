import streamlit as st
from sources import DEFAULT_BOOKS, search_pdfs, fetch_pdf_text

st.set_page_config(page_title="BTÜ Ders Avcısı", page_icon="📚", layout="wide")
st.title("📚 BTÜ Akıllı Ders Notu, Soru ve Çözüm Avcısı")

st.sidebar.header("Ders Seçimi")
course = st.sidebar.selectbox("Ders", list(DEFAULT_BOOKS.keys()))

st.write(f"Seçilen ders: **{course}**")
st.success("Asistan başarıyla çalışıyor! Kaynaklar yüklenmeye hazır.")
