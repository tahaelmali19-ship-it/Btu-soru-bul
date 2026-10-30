import streamlit as st
from sources import DEFAULT_BOOKS, search_pdfs, fetch_pdf_text, topic_window
from extractor import extract_qa
from notes import make_notes, solve_with_claude

st.set_page_config(page_title="BTÜ Ders Avcısı", page_icon="📚", layout="wide")
st.title("📚 BTÜ Akıllı Ders Notu, Soru ve Çözüm Avcısı")

with st.sidebar:
    course = st.selectbox("Ders", list(DEFAULT_BOOKS) + ["Diğer (elle gir)"])
    if course == "Diğer (elle gir)":
        course = st.text_input("Ders adı")
    books_txt = st.text_area(
        "Önerilen kitaplar (satır başına bir tane)",
        "\n".join(DEFAULT_BOOKS.get(course, [])),
        help="BTÜ ders bilgi paketindeki kaynak kitapları buraya yaz/düzenle.",
    )
    topic = st.text_input("Konu başlığı", "Matris Determinantı")
    api_key = st.text_input("Claude API anahtarı (opsiyonel)", type="password") or None
    max_pdfs = st.slider("Birleştirilecek en fazla PDF", 1, 5, 3)
    run = st.button("🔎 Kaynakları tara", type="primary")

state = st.session_state
for k, v in {"results": [], "qa": [], "notes": "", "solutions": {}, "meta": ""}.items():
    state.setdefault(k, v)

if run and topic:
    books = [b.strip() for b in books_txt.splitlines() if b.strip()]
    with st.spinner("Kaynaklar taranıyor, PDF'ler analiz ediliyor..."):
        results, combined, used = [], "", 0
        for b in books:
            for pdf in search_pdfs(b, topic):
                results.append(pdf)
                if pdf.get("url") and used < max_pdfs:
                    try:
                        text = fetch_pdf_text(pdf["url"])
                    except Exception:
                        continue
                    if len(text) > 200:
                        used += 1
                        combined += f"\n\n--- Kaynak {used}: {pdf['title']} ---\n" + topic_window(text, topic)
        state.results = results
        state.solutions = {}
        state.meta = f"{used} PDF birleştirildi."
        if combined:
            state.qa = extract_qa(combined, api_key=api_key)
            state.notes = make_notes(combined, topic, api_key)
        else:
            state.qa = []
            state.notes = "Uygun PDF metni bulunamadı veya arama sonucu boş döndü."

tab1, tab2, tab3 = st.tabs(["📁 Kaynaklar", "❓ Soru & Çözüm", "📝 Notlar"])

with tab1:
    if state.meta:
        st.caption(state.meta)
    if not state.results:
        st.info("Henüz tarama yapılmadı.")
    for r in state.results:
        st.markdown(f"- [{r['title']}]({r['url']})" if r.get("url") else "")
        if not r.get("url"):
            st.warning(r["title"])

with tab2:
    if not state.qa:
        st.info("Gösterilecek soru bulunamadı.")
    for i, item in enumerate(state.qa):
        with st.expander(f"Soru {i+1}: {item['question'][:90]}..."):
            st.markdown(item["question"])
            sol = item["solution"] if len(item["solution"]) > 20 else state.solutions.get(i, "")
            if sol:
                st.markdown("**Çözüm:**")
                st.markdown(sol)
            elif api_key:
                if st.button("Claude ile çözümü üret", key=f"solve{i}"):
                    with st.spinner("Çözülüyor..."):
                        state.solutions[i] = solve_with_claude(item["question"], api_key)
                    st.rerun()
            else:
                st.caption("Kaynakta çözüm yok. API anahtarı girersen üretebilirsin.")

with tab3:
    if state.notes:
        st.markdown(state.notes)
        st.download_button("Notları indir (.md)", state.notes,
                           file_name=f"{course}_{topic}_notlar.md", mime="text/markdown")
    else:
        st.info("Henüz not oluşturulmadı.")
