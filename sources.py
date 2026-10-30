DEFAULT_BOOKS = {
    "Endüstri Mühendisliğine Giriş": [
        "https://www.ie.boun.edu.tr/sites/default/files/inline-files/Intro_to_IE.pdf",
    ],
    "Yöneylem Araştırması / Lineer Programlama": [
        "https://www.sde.cite.iff.edu.br/wp-content/uploads/2020/05/Operations-Research-Applications-and-Algorithms.pdf",
    ],
}

def search_pdfs(query):
    return [
        {"title": f"{query} - Ders Kaynağı 1", "href": "https://example.com/pdf1.pdf"},
        {"title": f"{query} - Ders Kaynağı 2", "href": "https://example.com/pdf2.pdf"}
    ]

def fetch_pdf_text(url):
    return "Örnek PDF metin içeriği ve soru kalıpları..."
