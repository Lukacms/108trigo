##
## EPITECH PROJECT, 2022
## Visual Studio Live Share (Espace de travail)
## File description:
## multiply_matrix
##

from copy import copy


def multiply_matrix(
    matrix: list[list[float]], multiply: list[list[float]]
) -> list[list[float]]:
    product: list[list[float]] = []
    nb: float = 0
    i: int = 0
    size: int = len(matrix)

    while i < size:
        product.append([])
        for index in range(0, size, 1):
            nb = 0
            for j in range(0, size, 1):
                nb += matrix[i][j] * multiply[j][index]
            product[i].append(nb)
        i += 1
    return product


def power_matrix(matrix: list[list[float]], power: int) -> list[list[float]]:
    product: list[list[float]] = copy(matrix)

    for p in range(1, power, 1):
        product = multiply_matrix(matrix, product)
    return product
