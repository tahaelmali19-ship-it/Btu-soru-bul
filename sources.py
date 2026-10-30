BTU_DATABASE = {
    "Endüstri Mühendisliği": {
        "1. Sınıf": {
            "Genel Matematik I": {
                "ana_kaynak": "Thomas Calculus & BTU Matematik Paneli",
                "kaynak_url": "https://www.math.ust.hk/~machas/vector-calculus.pdf",
                "bolumler": {
                    "Limit ve Süreklilik": [
                        {
                            "soru": "Soru 1: f(x) = (x^2 - 4) / (x - 2) fonksiyonunun x -> 2 giderken limiti nedir?",
                            "cozum": "Pay çarpanlara ayrılır: (x-2)(x+2) / (x-2) = x+2. x=2 için limit 4 olarak bulunur.",
                            "kaynak_detay": "Thomas Calculus - Bölüm 2.2, Sayfa 112"
                        },
                        {
                            "soru": "Soru 2: lim_{x -> 0} (sin(x) / x) ifadesinin değerini bulunuz.",
                            "cozum": "Trigonometrik limit teoremine ve L'Hopital kuralına göre bu limit 1'e eşittir.",
                            "kaynak_detay": "Thomas Calculus - Bölüm 2.4, Sayfa 135"
                        },
                        {
                            "soru": "Soru 3: f(x) = |x| / x fonksiyonunun x -> 0 için sağdan ve soldan limitleri nedir?",
                            "cozum": "Sağdan limit 1, soldan limit -1'dir. Limitler farklı olduğu için x->0'da limit yoktur.",
                            "kaynak_detay": "BTU Örnek Soru Bankası - Analiz I"
                        }
                    ],
                    "Türev ve Uygulamaları": [
                        {
                            "soru": "Soru 1: f(x) = 3x^3 - 5x^2 + 7 fonksiyonunun türevi f'(x) nedir?",
                            "cozum": "Polinom türev kuralı uygulanır: f'(x) = 9x^2 - 10x",
                            "kaynak_detay": "Thomas Calculus - Bölüm 3.1, Sayfa 180"
                        }
                    ]
                }
            },
            "Genel Fizik I": {
                "ana_kaynak": "OpenStax University Physics Vol 1",
                "kaynak_url": "https://openstax.org/details/books/university-physics-volume-1",
                "bolumler": {
                    "Vektörler ve Kinematik": [
                        {
                            "soru": "Soru 1: İki vektörün skaler çarpımı hangi durumlarda sıfır olur?",
                            "cozum": "Vektörler birbirine dik (90 derece) açıyla olduğunda skaler çarpım sıfırdır.",
                            "kaynak_detay": "University Physics Vol 1 - Bölüm 2"
                        }
                    ]
                }
            },
            "Endüstri Mühendisliğine Giriş": {
                "ana_kaynak": "BTU Bölüm Ders Notları ve Endüstriyel Tasarım Rehberi",
                "kaynak_url": "https://www.ie.boun.edu.tr/sites/default/files/inline-files/Intro_to_IE.pdf",
                "bolumler": {
                    "Sistem ve Verimlilik Kavramları": [
                        {
                            "soru": "Soru 1: Endüstri mühendisliğinde toplam verimlilik formülü nasıl ifade edilir?",
                            "cozum": "Toplam Verimlilik = Toplam Çıktı / Toplam Girdi olarak ifade edilir.",
                            "kaynak_detay": "BTU IE Giriş Notları - Bölüm 1"
                        }
                    ]
                }
            }
        }
    },
    "Bilgisayar Mühendisliği": {
        "1. Sınıf": {
            "Genel Matematik I": {
                "ana_kaynak": "Thomas Calculus",
                "kaynak_url": "https://www.math.ust.hk/~machas/vector-calculus.pdf",
                "bolumler": {
                    "Limit ve Süreklilik": [
                        {
                            "soru": "Soru 1: lim_{x -> inf} (2x + 1) / (x - 3) limitini hesaplayınız.",
                            "cozum": "Pay ve payda x'in en yüksek derecesine (x) bölünür, sonuç 2 çıkar.",
                            "kaynak_detay": "Thomas Calculus - Bölüm 2.5"
                        }
                    ]
                }
            }
        }
    }
}
