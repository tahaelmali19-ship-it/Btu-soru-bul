"""Soru/çözüm ayıklama: Claude ile akıllı ayıklama, olmazsa regex yedeği."""
import json
import re
import anthropic
from modules.notes import MODEL

Q_SPLIT = re.compile(
    r"(?im)^\s*(?:problem|exercise|example|soru|örnek|alıştırma)\s*\d+(?:\.\d+)*\s*[.:)\-]?"
)
S_SPLIT = re.compile(r"(?im)^\s*(?:solution|solving|answer|çözüm|cevap)\s*[.:]?")


def _extract_with_llm(text: str, api_key: str, max_items: int) -> list[dict]:
    try:
        client = anthropic.Anthropic(api_key=api_key)
        prompt = (
            "Aşağıdaki metinden akademik soruları ve varsa çözümlerini çıkar. "
            "Yanıtı sadece JSON listesi olarak ver, başka metin ekleme. "
            'Format: [{"question": "...", "solution": "..."}] (çözüm yoksa boş string).\n\n'
            f"Metin:\n{text[:15000]}"
        )
        msg = client.messages.create(
            model=MODEL, max_tokens=3000, messages=[{"role": "user", "content": prompt}]
        )
        out = "".join(b.text for b in msg.content if b.type == "text")
