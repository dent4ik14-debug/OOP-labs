import pytest
from laba4_OOP import NPC, Text, Word, Sentence, Letter


def test_text_normalization():
    """Перевірка видалення зайвих пробілів та табуляцій"""
    raw_input = "Це   тест.\tНове  речення."
    text_obj = Text(raw_input)
    assert str(text_obj) == "Це тест. Нове речення."


def test_hierarchy_structure():
    """Перевірка ієрархії: Text -> Sentence -> Word -> Letter"""
    input_str = "Hi."
    text_obj = Text(input_str)

    assert isinstance(text_obj.sentences[0], Sentence)
    assert isinstance(text_obj.sentences[0].elements[0], Word)
    assert isinstance(text_obj.sentences[0].elements[0].letters[0], Letter)
    assert str(text_obj.sentences[0].elements[0].letters[0]) == "H"


def test_npc_equality():
    """Перевірка рівності NPC (враховуючи, що поля тепер є об'єктами Word)"""
    npc1 = NPC("Goblin", 5, 50, False, "forest")
    npc2 = NPC("Goblin", 5, 50, False, "forest")
    npc3 = NPC("Orc", 5, 50, False, "forest")

    assert npc1 == npc2
    assert npc1 != npc3
    assert npc1 != "Not an NPC"


def test_npc_sorting_logic():
    """Перевірка сортування: спочатку за level (asc), потім за health (desc)"""
    npc_list = [
        NPC("Alpha", 5, 100, False, "cave"),
        NPC("Beta", 5, 200, False, "cave"),
        NPC("Gamma", 10, 50, False, "cave"),
    ]

    npc_list.sort(key=lambda npc: (npc.level, -npc.health))

    assert str(npc_list[0].name) == "Beta"
    assert str(npc_list[1].name) == "Alpha"
    assert str(npc_list[2].name) == "Gamma"


def test_npc_repr_with_objects():
    """Перевірка строкового представлення (метод __repr__)"""
    npc = NPC("Dragon", 25, 500, False, "mount")
    res = repr(npc)
    assert "Dragon" in res
    assert "25" in res
    assert "mount" in res


def test_word_to_string():
    """Перевірка перетворення об'єкта Word назад у рядок"""
    word = Word("Test")
    assert str(word) == "Test"
    assert len(word.letters) == 4