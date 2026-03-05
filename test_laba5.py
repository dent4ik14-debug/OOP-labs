import pytest
from laba5_OOP import Train, Suit, Berth, Intercity, Carriage  # Заміни your_filename


def test_train_counting():
    """Перевірка правильності підрахунку загальної кількості пасажирів та багажу"""
    train = Train()
    train.add_carriage([Suit(10, 50), Berth(20, 30)])

    assert "30" in train.counting_number_of_passengers()
    assert "80" in train.get_total_luggage()


def test_sorting_by_comfort():
    """Перевірка сортування вагонів за рівнем комфорту (від більшого до меншого)"""
    train = Train()
    low_comfort = Berth(50, 20)
    high_comfort = Suit(10, 100)
    mid_comfort = Intercity(30, 40)

    train.add_carriage([low_comfort, high_comfort, mid_comfort])
    train.sort_carriages()

    assert train.carriages[0].comfort_level == 5
    assert train.carriages[1].comfort_level == 2
    assert train.carriages[2].comfort_level == 1


def test_find_carriages_by_range():
    """Перевірка пошуку вагонів у заданому діапазоні пасажирів"""
    train = Train()
    c1 = Suit(10, 50)
    c2 = Berth(50, 20)
    c3 = Intercity(25, 30)

    train.add_carriage([c1, c2, c3])
    found = train.find_carriages_by_passengers(10, 30)

    assert len(found) == 2
    assert c1 in found
    assert c3 in found
    assert c2 not in found


def test_negative_values_exception():
    """Перевірка захисту від від'ємних значень у конструкторі"""
    with pytest.raises(ValueError, match="не може бути від'ємною"):
        Suit(-5, 10)


def test_add_invalid_object():
    """Перевірка, що до потяга не можна додати об'єкт, який не є вагоном"""
    train = Train()
    train.add_carriage("Я просто рядок")
    assert len(train.carriages) == 0