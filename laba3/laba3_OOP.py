class NPC():
    """
        Клас для представлення неігрового персонажа (NPC).
        Містить 5 полів згідно з завданням.
    """
    def __init__(self, name, level, health, is_friend, place):
        self.name = name
        self.level = level
        self.health = health
        self.is_friend = is_friend
        self.place = place
    def __eq__(self, other):
        """
            Перевизначення оператора порівняння для пошуку ідентичного об'єкта.
            Об'єкт вважається ідентичним, якщо всі його поля збігаються.
        """
        if not isinstance(other, NPC):
            return False
        else:
            return (self.name == other.name and
                    self.level == other.level and
                    self.health == other.health and
                    self.is_friend == other.is_friend and
                    self.place == other.place)

    def __repr__(self):
        """Повертає строкове представлення об'єкта для зручного виводу."""
        return f"NPC({self.name}, {self.level}, {self.is_friend}, {self.place})"

def main():
    """Виконавчий метод програми."""
    npc_list = [
        NPC("Dragon",25 ,500, False, "mount"),
        NPC("Goblin",5 ,50, False, "forest"),
        NPC("Merchant", 30, 100, True, "city"),
        NPC("Ogr", 10, 750, False, "forest"),
        NPC("Leshy", 15, 250, False, "forest"),
    ]
    print("Початковий список:")
    for npc in npc_list:
        print(npc)

    npc_list.sort(key=lambda npc: (npc.level, -npc.health))
    print("\nСписок після сортування:")
    for npc in npc_list:
        print(npc)

    search_target = NPC("Dragon",25 ,500, False, "mount")
    if search_target in npc_list:
        print(f"\n{search_target} Знайдено")
    else:
        print("Не знайдено")

if __name__ == "__main__":
    main()