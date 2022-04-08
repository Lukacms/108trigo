##
## EPITECH PROJECT, 2022
## 108trigo
## File description:
## matrix_addition
##


def matrix_addition(
    matrix: list[list[float]], to_add: list[list[float]]
) -> list[list[float]]:
    results: list[list[float]] = []
    len_matrix: int = len(matrix)

    for i in range(0, len_matrix):
        results.append([])
        for j in range(0, len_matrix, 1):
            results[i].append(matrix[i][j] + to_add[i][j])
    return results


def matrix_substraction(
    matrix: list[list[float]], to_add: list[list[float]]
) -> list[list[float]]:
    results: list[list[float]] = []
    len_matrix: int = len(matrix)

    for i in range(0, len_matrix):
        results.append([])
        for j in range(0, len_matrix, 1):
            results[i].append(matrix[i][j] - to_add[i][j])
    return results
