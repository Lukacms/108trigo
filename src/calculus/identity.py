##
## EPITECH PROJECT, 2022
## 108trigo
## File description:
## identity
##


def identity_matrix(size: int) -> list[list[float]]:
    identity: list[list[float]] = []
    count: int = 0

    for i in range(0, size, 1):
        identity.append([])
        for j in range(0, size, 1):
            identity[i].append(0)
        identity[i][count] = 1
        count += 1
    return identity
