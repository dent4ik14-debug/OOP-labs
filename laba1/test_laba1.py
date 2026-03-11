import pytest
import numpy as np
from laba1_OOP import CalculatorMatrix

def test_multiplication_logic():
    calc = CalculatorMatrix(20)
    matrix_b = np.array([[1, 2], [3, 4]], dtype=np.float64)
    result = calc.perform_first_action(matrix_b, 2)
    expected = np.array([[2, 4], [6, 8]])
    assert np.array_equal(result, expected)

def test_columns_mean_logic():
    calc = CalculatorMatrix(20)
    matrix_c = np.array([[10, 20], [30, 40]], dtype=np.float64)
    result = calc.perform_second_action(matrix_c)
    assert np.array_equal(result, np.array([20.0, 30.0]))