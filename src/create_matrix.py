##
## EPITECH PROJECT, 2022
## 108trigo
## File description:
## create_matrix
##

from src.parse_args import Arguments
from math import sqrt


def create_matrix(arguments: Arguments) -> list[list[float]]:
    len_matrix: int = int(sqrt(len(arguments.mat)))
    matrix: list[list[float]] = []
    count: int = 0

    for i in range(0, len_matrix, 1):
        matrix.append([])
        for j in range(0, len_matrix, 1):
            matrix[i].append(int(arguments.mat[count]))
            count += 1
    return matrix
