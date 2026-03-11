import pytest
import io
from laba2_OOP import TextAnalyzer

VALID_ID = 20

def test_initialization_valid():
    """Перевірка правильної ініціалізації при вірному номері залікової"""
    analyzer = TextAnalyzer(VALID_ID, "Тест?", 5)
    assert analyzer.c3 == 2
    assert analyzer.c17 == 3

def test_initialization_invalid_variant():
    """Перевірка, чи виникає ValueError, якщо варіант не збігається"""
    with pytest.raises(ValueError, match="не збігається з розрахунками"):
        TextAnalyzer(10, "Текст", 3)

def test_analyze_logic():
    """Перевірка пошуку слів заданої довжини у питальних реченнях"""
    text = "Скільки це коштує? Це коштує дорого. Де купити?"
    analyzer = TextAnalyzer(VALID_ID, text, 2)
    result = analyzer.analyze()
    assert result == ["де", "це"]


def test_analyze_no_duplicates():
    """Перевірка, що слова не повторюються (регістронезалежно)"""
    text = "Хто там? ХТО ТАМ?"
    analyzer = TextAnalyzer(VALID_ID, text, 3)
    result = analyzer.analyze()
    assert result == ["там", "хто"]

def test_analyze_empty_text():
    """Перевірка обробки порожнього тексту"""
    analyzer = TextAnalyzer(VALID_ID, "", 5)
    result = analyzer.analyze()
    assert "Текст порожній" in result

def test_analyze_negative_length():
    """Перевірка обробки некоректної довжини слова"""
    analyzer = TextAnalyzer(VALID_ID, "Текст?", -1)
    result = analyzer.analyze()
    assert "Довжина слова повинна бути додатною" in result

def test_analyze_no_questions():
    """Перевірка випадку, коли питальних речень немає"""
    text = "Це звичайне речення. Тут немає питань."
    analyzer = TextAnalyzer(VALID_ID, text, 2)
    assert analyzer.analyze() == []