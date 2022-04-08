##
## EPITECH PROJECT, 2022
## Visual Studio Live Share (Espace de travail)
## File description:
## exponentielle
##

from copy import copy
from math import factorial

from src.calculus.multiply_matrix import power_matrix
from src.calculus.matrix_division import division
from src.calculus.identity import identity_matrix
from src.calculus.matrix_addition import matrix_addition


def compare(matrix: list[list[float]], before: list[list[float]]) -> float:
    result: float = 0.0
    tmp: float = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            tmp = matrix[i][j] - before[i][j]
            if abs(tmp) > result:
                result = abs(tmp)
    return result


def positive_exponential(matrix: list[list[float]]) -> list[list[float]]:
    result: list[list[float]] = identity_matrix(len(matrix))
    save: list[list[float]] = copy(matrix)
    epsilon: float = 1
    c: int = 1

    while epsilon > 0.000001:
        save = division(power_matrix(matrix, c), factorial(c))
        save = matrix_addition(result, save)
        epsilon = compare(result, save)
        if epsilon > 0.000001:
            result = save
        c += 1
    return result


def negative_exponential(matrix: list[list[float]]) -> list[list[float]]:
    result: list[list[float]] = []

    for i in range(0, len(matrix)):
        result.append([])
        for j in range(0, len(matrix[0])):
            result[i].append(matrix[i][j] * -1)
    return positive_exponential(result)
