# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence
import re

REGEX_MUL = r"mul\(\d{1,3},\d{1,3}\)"
REGEX_C_MUL = re.compile(REGEX_MUL)
REGEX_MUL_OPERANDS = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def get_mul_operands(mul_str):
    match = REGEX_MUL_OPERANDS.search(mul_str)
    return tuple(map(int, match.groups())) if match else ()
