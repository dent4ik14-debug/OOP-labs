import numpy as np

class CalculatorMatrix:
    def __init__(self, student_number):
        self.student_number = student_number
        self.c5 = student_number % 5
        self.c7 = student_number % 7
        self.c11 = student_number % 11

        if not (self.c5 == 0 and self.c7 == 6 and self.c11 == 9):
            raise ValueError(f"Варіант (C5={self.c5}, C7={self.c7}, C11={self.c11}) не збігається з розрахунками.")

    def get_matrix_element_type(self):
        return np.float64

    def perform_first_action(self, matrix_b, scalar):
        if not isinstance(matrix_b, np.ndarray):
            raise TypeError("Вхідний об'єкт для першої дії має бути матрицею NumPy.")
        return matrix_b * scalar

    def perform_second_action(self, matrix_c):
        if not isinstance(matrix_c, np.ndarray):
            raise TypeError("Вхідний об'єкт для другої дії має бути матрицею NumPy.")
        if matrix_c.size == 0:
            raise ValueError("Матриця порожня, неможливо обчислити середнє.")
        return np.mean(matrix_c, axis=0)

    def execute(self, rows=3, cols=3, scalar=5.5):
        try:
            dtype = self.get_matrix_element_type()
            matrix_b = np.random.uniform(1.0, 100.0, size=(rows, cols)).astype(dtype)
            print(f"\n1. Матриця B (тип {dtype}):\n{matrix_b}")
            matrix_c = self.perform_first_action(matrix_b, scalar)
            print(f"\n2. Результат першої дії (C = B * {scalar}):\n{matrix_c}")
            result = self.perform_second_action(matrix_c)
            print(f"\n3. Результат другої дії (Середнє стовпців):\n{result.round(4)}")

        except TypeError as te:
            print(f"Помилка типу даних: {te}")
        except ValueError as ve:
            print(f"Помилка у значеннях: {ve}")
        except Exception as e:
            print(f"Виникла неочікувана помилка: {e}")

if __name__ == "__main__":
    try:
        calc = CalculatorMatrix(20)
        calc.execute()
    except Exception as init_error:
        print(f"Помилка при ініціалізації: {init_error}")