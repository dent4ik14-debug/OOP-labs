import pytest
from laba3_OOP import NPC


def test_npc_equality():
    """Перевірка, що два об'єкти з однаковими даними вважаються рівними"""
    npc1 = NPC("Goblin", 5, 50, False, "forest")
    npc2 = NPC("Goblin", 5, 50, False, "forest")
    npc3 = NPC("Goblin", 10, 50, False, "forest")

    assert npc1 == npc2
    assert npc1 != npc3
    assert npc1 != "Not an NPC"


def test_npc_sorting_logic():
    """Перевірка сортування: спочатку за level (asc), потім за health (desc)"""
    npc_list = [
        NPC("LowLevelStrong", 5, 100, False, "cave"),
        NPC("LowLevelWeak", 5, 50, False, "cave"),
        NPC("HighLevel", 10, 200, False, "cave"),
    ]

    npc_list.sort(key=lambda npc: (npc.level, -npc.health))

    assert npc_list[0].name == "LowLevelStrong"
    assert npc_list[1].name == "LowLevelWeak"
    assert npc_list[2].name == "HighLevel"


def test_npc_repr():
    """Перевірка строкового представлення об'єкта"""
    npc = NPC("Dragon", 25, 500, False, "mount")
    expected_repr = "NPC(Dragon, 25, False, mount)"
    assert repr(npc) == expected_repr


def test_search_in_list():
    """Перевірка пошуку об'єкта у списку (використовує __eq__)"""
    npc_list = [
        NPC("Merchant", 30, 100, True, "city"),
        NPC("Ogr", 10, 750, False, "forest")
    ]
    search_target = NPC("Merchant", 30, 100, True, "city")

    assert search_target in npc_list