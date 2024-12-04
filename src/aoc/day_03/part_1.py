# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence
import math
from pathlib import Path

from aoc.common import get_lines
from aoc.day_03.common import REGEX_C_MUL, get_mul_operands


def get_mul(line):
    matches = REGEX_C_MUL.finditer(line)
    for match in matches:
        yield match.group()


def get_added_mul(lines):
    added_mul = 0
    for line in lines:
        for mul in get_mul(line):
            added_mul += math.prod(get_mul_operands(mul))
    return added_mul


def solve():
    # pylint: disable=R0801
    aoc_root = Path(__file__).parents[3]
    input_path = aoc_root / "inputs" / "day_03" / "parts_1_2.txt"
    return get_added_mul(get_lines(input_path))


if __name__ == "__main__":
    print("Day 03, Part 1:", solve())
