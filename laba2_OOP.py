import io
import re

class TextAnalyzer:
    def __init__(self, student_number, text, word_length):
        self.c3 = student_number % 3
        self.c17 = student_number % 17
        if not (self.c3 == 2 and self.c17 == 3):
            raise ValueError(f"Варіант (C3={self.c3}, C17={self.c17}) не збігається з розрахунками.")
        self.buffer = io.StringIO(text)
        self.word_length = word_length

    def analyze(self):
        try:
            content = self.buffer.getvalue()

            if not content:
                raise ValueError("Текст порожній.")
            if self.word_length <= 0:
                raise ValueError("Довжина слова повинна бути додатною.")

            sentences = re.findall(r'[^.!?]+\?', content)

            unique_words = set()
            for sentence in sentences:
                words = re.findall(r'\b\w+\b', sentence)
                for word in words:
                    if len(word) == self.word_length:
                        unique_words.add(word.lower())

            return sorted(list(unique_words))

        except Exception as e:
            return f"Помилка при обробці: {e}"


def main():
    try:
        student_id_str = input("Введіть номер залікової книжки: ")
        if not student_id_str.isdigit():
            raise ValueError("Номер залікової книжки має бути цілим числом.")
        student_number = int(student_id_str)

        print("\nВведіть текст (для завершення вводу натисніть Enter):")
        user_text = input("> ")

        length_str = input("Введіть довжину шуканих слів: ")
        if not length_str.isdigit():
            raise ValueError("Довжина слова має бути цілим числом.")
        target_length = int(length_str)

        analyzer = TextAnalyzer(student_number, user_text, target_length)
        result = analyzer.analyze()

        print("\n--- Результат обробки ---")
        if isinstance(result, list):
            if result:
                print(f"Слова довжиною {target_length} у питальних реченнях:")
                for word in result:
                    print(f"- {word}")
            else:
                print("Слів, що відповідають умовам, не знайдено.")
        else:
            print(result)

    except ValueError as ve:
        print(f"\nПомилка вхідних даних: {ve}")
    except Exception as e:
        print(f"\nВиникла непередбачена помилка: {e}")
    finally:
        print("\nРоботу програми завершено.")


if __name__ == "__main__":
    main()