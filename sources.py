DEFAULT_BOOKS = {
    "Endüstri Mühendisliğine Giriş": [
        "https://www.ie.boun.edu.tr/sites/default/files/inline-files/Intro_to_IE.pdf"
    ]
}

def search_pdfs(query):
    return [
        {"title": "Ders Kaynağı 1", "href": "https://example.com/pdf1.pdf"}
    ]

def fetch_pdf_text(url):
    return "Örnek PDF metin içeriği..."
