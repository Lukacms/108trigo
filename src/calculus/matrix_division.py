##
## EPITECH PROJECT, 2022
## 108trigo
## File description:
## division
##

from copy import copy


def division(matrix: list[list[float]], divide: int) -> list[list[float]]:
    result: list[list[float]] = []
    len_matrix: int = len(matrix)

    for i in range(0, len_matrix, 1):
        result.append([])
        for j in range(0, len_matrix, 1):
            result[i].append(matrix[i][j] / divide)
    return result
