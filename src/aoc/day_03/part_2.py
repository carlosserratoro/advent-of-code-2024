# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence
import math
import re
from pathlib import Path

from aoc.common import get_lines
from aoc.day_03.common import REGEX_MUL, get_mul_operands

# Not using Enum here because of the named groups in the regex below.
I_DO = "DO"
I_DONT = "DONT"
I_MUL = "MUL"

REGEX_DO = r"do\(\)"
REGEX_C_DO = re.compile(REGEX_DO)
REGEX_DONT = r"don't\(\)"
REGEX_C_DONT = re.compile(REGEX_DONT)
REGEX_INSTRUCTIONS = (
    rf"(?P<{I_DO}>{REGEX_DO})|(?P<{I_DONT}>{REGEX_DONT})|(?P<{I_MUL}>{REGEX_MUL})"
)
REGEX_C_INSTRUCTIONS = re.compile(REGEX_INSTRUCTIONS)


def get_instructions(line):
    matches = REGEX_C_INSTRUCTIONS.finditer(line)
    for match in matches:
        if match.group(I_DO):
            yield I_DO, None
        elif match.group(I_DONT):
            yield I_DONT, None
        else:  # if match.group(I_MUL):
            yield I_MUL, match.group()


def get_added_mul(lines):
    added_mul = 0
    instructions_enabled = True
    for line in lines:
        for instruction_type, instruction in get_instructions(line):
            if instruction_type == I_DO:
                instructions_enabled = True
            elif instruction_type == I_DONT:
                instructions_enabled = False
            elif instruction_type == I_MUL and instructions_enabled:
                added_mul += math.prod(get_mul_operands(instruction))
    return added_mul


def solve():
    # pylint: disable=R0801
    aoc_root = Path(__file__).parents[3]
    input_path = aoc_root / "inputs" / "day_03" / "parts_1_2.txt"
    return get_added_mul(get_lines(input_path))


if __name__ == "__main__":
    print("Day 03, Part 2:", solve())
