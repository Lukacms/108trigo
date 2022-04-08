##
## EPITECH PROJECT, 2022
## 108trigo
## File description:
## display
##


from decimal import ROUND_HALF_UP


def display_result(matrix: list[list[float]]) -> None:
    size: int = len(matrix)
    nb: float = 0
    tmp: str

    for i in range(0, size):
        for j in range(0, size):
            # nb = round(matrix[i][j], 3)
            # tmp = str(nb)
            # if tmp[len(tmp) - 1] == "5":
            #     nb += 0.001
            # if nb == -0.00:
            #     nb = 0.00
            if round(matrix[i][j], 3) == -0.00:
                matrix[i][j] = 0.00
            print(f"{matrix[i][j]:.2f}", end="")
            if j < size - 1:
                print("\t", end="")
        print("")
