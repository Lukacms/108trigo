##
## EPITECH PROJECT, 2022
## 106bombyx
## File description:
## parse_args
##

from argparse import ArgumentError, ArgumentTypeError, ArgumentParser
from math import sqrt
from typing import NamedTuple
from sys import argv

from sys import exit


class Arguments(NamedTuple):
    fun: str
    mat: list[str]


def valid_arg(arg: str) -> int:
    nb: int = 0

    try:
        nb = int(arg)
    except ValueError:
        raise ArgumentTypeError(f"Parameter {arg} isn't an integer")
    return nb


def parse_args() -> Arguments:
    parser = ArgumentParser()

    parser.add_argument(
        "fun",
        type=str,
        choices=["EXP", "COS", "SIN", "COSH", "SINH"],
        help=" function to be applied",
    )
    parser.add_argument(
        "mat", type=valid_arg, help="coeficients of the matrix", nargs="+"
    )

    try:
        args = parser.parse_args()
    except SystemExit:
        exit(84)
    nb: float = float(sqrt(len(argv) - 2))
    if round(nb) != nb:
        print(
            f"The matrix isn't complete: {len(argv) - 2} arguments instead of {pow(round(nb), 2)}"
        )
        exit(84)
    return Arguments(args.fun, args.mat)
