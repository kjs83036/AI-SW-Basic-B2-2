"""String utility functions."""

def capitalize_words(text: str) -> str:
    """각 단어의 첫 글자를 대문자로 변환합니다."""
    if not text:
        return ""
    return " ".join(word.capitalize() for word in text.split(" "))

def reverse_string(text: str) -> str:
    """문자열을 반전합니다."""
    return text[::-1]

def strip_all_whitespace(text: str) -> str:
    """모든 공백(탭, 줄바꿈 포함)을 제거합니다."""
    if not text:
        return ""
    return "".join(text.split())
