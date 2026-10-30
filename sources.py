DEFAULT_BOOKS = {
    "Endüstri Mühendisliğine Giriş": {
        "kategoriler": ["Genel Kavramlar", "Sistem Analizi", "Üretim ve Verimlilik"],
        "kaynaklar": [
            {"title": "Boğaziçi Üniversitesi - Intro to IE", "href": "https://www.ie.boun.edu.tr/sites/default/files/inline-files/Intro_to_IE.pdf"},
            {"title": "BTÜ Ders Notu - Endüstri Mühendisliğine Giriş Rehberi", "href": "https://example.com/btu_ie_giris.pdf"}
        ]
    },
    "Yöneylem Araştırması / Lineer Programlama": {
        "kategoriler": ["Lineer Programlama (Simplex)", "Ulaştırma ve Atama Modelleri", "Ağ Modelleri", "Bütünleşik Optimizasyon"],
        "kaynaklar": [
            {"title": "Operations Research: Applications and Algorithms (Winston)", "href": "https://www.sde.cite.iff.edu.br/wp-content/uploads/2020/05/Operations-Research-Applications-and-Algorithms.pdf"},
            {"title": "BTÜ Yöneylem Ders Notları ve Çözümlü Problemler", "href": "https://example.com/btu_yoneylem.pdf"}
        ]
    },
    "Matematik / Analiz": {
        "kategoriler": ["Limit ve Süreklilik", "Türev ve Uygulamaları", "İntegral ve Alan", "Çok Katlı İntegraller"],
        "kaynaklar": [
            {"title": "HKUST - Vector Calculus & Mathematical Analysis", "href": "https://www.math.ust.hk/~machas/vector-calculus.pdf"},
            {"title": "BTÜ Matematik Bölümü Örnek Soru Bankası", "href": "https://example.com/btu_matematik.pdf"}
        ]
    },
    "Fizik": {
        "kategoriler": ["Mekanik ve Vektörler", "Newton Kanunları", "İş ve Enerji", "Momentum"],
        "kaynaklar": [
            {"title": "OpenStax University Physics Volume 1", "href": "https://openstax.org/details/books/university-physics-volume-1"},
            {"title": "BTÜ Fizik Laboratuvar ve Problem Kılavuzu", "href": "https://example.com/btu_fizik.pdf"}
        ]
    }
}

def search_pdfs(course_name, category, query):
    # Seçilen derse ve kategoriye ait kaynakları ve yapay zeka analizini simüle eder
    course_data = DEFAULT_BOOKS.get(course_name, {"kaynaklar": [{"title": "Genel Akademik Kaynak", "href": "https://example.com"}]})
    return course_data["kaynaklar"]
