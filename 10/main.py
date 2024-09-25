"""
6. Написать функцию, которая принимает матрицу и воз-
вращает её определитель.
"""

import numpy as np

def calculate_determinant(matrix):
    np_matrix = np.array(matrix)
    determinant = np.linalg.det(np_matrix)
    return determinant

def calculate_determinant_without_numpy(matrix):
    # проверяю что строго длинна каждой строки одинаковая и равна кол-ву столбцов
    for i in matrix:
        if len(matrix) != len(i):
            raise ValueError("Матрица должна быть квадратной")

    if len(matrix) == 1:
        return matrix[0][0]
    
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    determinant = 0
    for col in range(len(matrix)):
        # раскладываю по первой строке
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        # сокращаю матрицу и вычиляю заного ее определитель
        det_minor = calculate_determinant(minor)
        # ((-1) ** col) чередую знаки при разложении лапласа
        # далее умножаю на текущий элемент строки, по которому раскладываю
        # и умножаю на вычесленный минор
        determinant += ((-1) ** col) * matrix[0][col] * det_minor
    
    return determinant

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
det = calculate_determinant(matrix)
print("Определитель матрицы:", det)

print("------------------------------------------------")

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
det = calculate_determinant_without_numpy(matrix) # рекурсивная функция вычисления
print("Определитель матрицы:", det)