##
## EPITECH PROJECT, 2022
## 108trigo
## File description:
## calculate_cos
##

from copy import copy
from math import factorial

from src.calculus.multiply_matrix import power_matrix, multiply_matrix
from src.calculus.matrix_division import division
from src.calculus.identity import identity_matrix
from src.calculus.matrix_addition import matrix_addition, matrix_substraction
from src.calculus.matrix_division import division
from src.calculus.multiply_matrix import multiply_matrix
from src.functions.exponential import positive_exponential, negative_exponential
from src.functions.exponential import compare


def calculate_cos(matrix: list[list[float]]) -> list[list[float]]:
    result: list[list[float]] = identity_matrix(len(matrix))
    save: list[list[float]] = copy(matrix)
    epsilon: float = 1
    c: int = 2
    is_addition: int = 1

    while epsilon > 0.0001:
        save = division(power_matrix(matrix, c), factorial(c))
        if is_addition % 2 == 0:
            save = matrix_addition(result, save)
        elif is_addition % 2 == 1:
            save = matrix_substraction(result, save)
        epsilon = compare(result, save)
        if epsilon > 0.0001:
            result = save
        c += 2
        is_addition += 1
    return result


def calculate_cosh(matrix: list[list[float]]) -> list[list[float]]:
    result: list[list[float]] = []

    result = division(
        matrix_addition(positive_exponential(matrix), negative_exponential(matrix)), 2
    )
    return result
