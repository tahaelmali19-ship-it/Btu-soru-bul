"""Kaynak kitap listesi, açık PDF arama (önbellekli) ve metin çıkarma."""
import io
import requests
import streamlit as st
from duckduckgo_search import DDGS
from pypdf import PdfReader

DEFAULT_BOOKS = {
    "Doğrusal Cebir": ["Elementary Linear Algebra Anton", "Linear Algebra and Its Applications Lay"],
    "Fizik 1": ["University Physics Young Freedman", "Physics for Scientists and Engineers Serway"],
    "Yöneylem Araştırması": ["Introduction to Operations Research Hillier Lieberman", "Operations Research Taha"],
    "Programlamaya Giriş": ["Think Python Downey", "Python Programming Zelle"],
}

SEARCH_TERMS = "problems solutions filetype:pdf"


@st.cache_data(ttl=3600, show_spinner=False)
def _search_cached(book: str, topic: str, max_results: int) -> list[dict]:
    # Hata fırlatırsa Streamlit sonucu önbelleğe ALMAZ.
    with DDGS() as ddgs:
        res = list(ddgs.text(f"{book} {topic} {SEARCH_TERMS}", max_results=max_results))
    return [{"title": r.get("title", ""), "url": r.get("href", "")} for r in res]

