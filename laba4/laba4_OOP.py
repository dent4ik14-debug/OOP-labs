import re

class Letter:
    """Клас для представлення окремої літери."""
    def __init__(self, char):
        self.char = char
    def __str__(self):
        return self.char


class Punctuation:
    """Клас для представлення розділових знаків."""
    def __init__(self, mark):
        self.mark = mark
    def __str__(self):
        return self.mark


class Word:
    """Клас для представлення слова (масив літер)."""
    def __init__(self, word_str):
        self.letters = [Letter(c) for c in word_str]
    def __str__(self):
        return "".join(str(l) for l in self.letters)


class Sentence:
    """Клас для представлення речення (масив слів та знаків)."""
    def __init__(self, sentence_str):
        self.elements = []
        tokens = re.findall(r"[\w']+|[.,!?;:-]", sentence_str)
        for token in tokens:
            if re.match(r"[\w']+", token):
                self.elements.append(Word(token))
            else:
                self.elements.append(Punctuation(token))
    def __str__(self):
        result = ""
        for i, elem in enumerate(self.elements):
            if i > 0 and isinstance(elem, Word):
                result += " "
            result += str(elem)
        return result


class Text:
    """Клас для представлення тексту (масив речень)."""
    def __init__(self, raw_text):
        cleaned = re.sub(r'[ \t]+', ' ', raw_text).strip()

        sentence_list = re.split(r'(?<=[.!?])\s+', cleaned)
        self.sentences = [Sentence(s) for s in sentence_list if s]

    def __str__(self):
        return " ".join(str(s) for s in self.sentences)


class NPC:
    """Клас NPC, де текстові поля зберігаються як об'єкти Text/Word."""

    def __init__(self, name, level, health, is_friend, place):
        self.name = Word(name)
        self.level = level
        self.health = health
        self.is_friend = is_friend
        self.place = Word(place)

    def __eq__(self, other):
        if not isinstance(other, NPC): return False
        return (str(self.name) == str(other.name) and
                self.level == other.level and
                self.health == other.health and
                self.is_friend == other.is_friend and
                str(self.place) == str(other.place))

    def __repr__(self):
        return f"NPC(Name: {self.name}, Lvl: {self.level}, Place: {self.place})"


class Lab4Processor:
    """Клас, що містить виконавчий метод для обробки NPC."""
    @staticmethod
    def run():
        raw_input = "Dragon   25  \t mount. Goblin 5 forest. Merchant 30 city."
        print(f"Вхідний текст для обробки:\n'{raw_input}'\n")

        processed_text = Text(raw_input)
        print(f"Текст після нормалізації:\n{processed_text}\n")

        npc_list = [
            NPC("Dragon", 25, 500, False, "mount"),
            NPC("Goblin", 5, 50, False, "forest"),
            NPC("Merchant", 30, 100, True, "city"),
            NPC("Ogr", 10, 750, False, "forest"),
            NPC("Leshy", 15, 250, False, "forest"),
        ]

        npc_list.sort(key=lambda x: (x.level, -x.health))

        print("Відсортований список NPC:")
        for npc in npc_list:
            print(npc)

        target = NPC("Dragon", 25, 500, False, "mount")
        found = any(npc == target for npc in npc_list)
        print(f"\nПошук {target}: {'Знайдено' if found else 'Не знайдено'}")


if __name__ == "__main__":
    Lab4Processor.run()