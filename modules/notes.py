"""Not üretimi ve LaTeX çözüm biçimlendirme."""
import re
import anthropic

MODEL = "claude-sonnet-5-5"


def _ask(api_key: str, system: str, prompt: str, max_tokens: int = 1500) -> str:
    try:
        client = anthropic.Anthropic(api_key=api_key)
        msg = client.messages.create(
            model=MODEL, max_tokens=max_tokens, system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        return "".join(b.text for b in msg.content if b.type == "text")
    except Exception as e:
        return f"Claude API hatası: {e}"


def make_notes(text: str, topic: str, api_key: str | None) -> str:
    if api_key:
        return _ask(
            api_key,
            "Üniversite öğrencisi için sınav öncesi hızlı tekrar notu hazırlarsın. Türkçe yaz. "
            "Sadece tanım, formül (LaTeX, $...$), işlem adımları ve sık yapılan hatalar. Kısa ve maddeli.",
