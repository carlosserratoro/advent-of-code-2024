# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.common import get_lines

OPS = ["+", "*"]


def parse_calibration_equation(line):
    fields = line.split()
    result = int(fields[0].rstrip(":"))
    operands = list(map(int, fields[1:]))
    return result, operands


def apply(operands, operators):
    """Apply the operators in between the operands, left-to-right order.

    This is a Polish notation if we reverse the operators and put them
    before the operands and then we evaluate it normally.
    """
    # Example: If operands were 3, 2, 7, and operands were + *
    # then in Polish notation it would be * + 3 2 7 for (3 + 2) * 7:
    polish = list(reversed(operators)) + operands
    stack = []
    for elem in reversed(polish):
        if elem in OPS:
            if elem == "+":
                stack.append(stack.pop() + stack.pop())
            else:  # if elem == '+':
                stack.append(stack.pop() * stack.pop())
        else:
            stack.append(elem)
    return stack.pop()


def check_operands_combine_well(result, operands):
    """Check if the operands can yield the result if properly combined."""

    def _check(result, operators_list, pos):
        if pos == len(operands) - 1 and apply(operands, operators_list) == result:
            return True
        if pos == len(operands) - 1:
            return False
        for op in OPS:
            operators_list.append(op)
            if _check(result, operators_list, pos + 1):
                return True
            operators_list.pop()
        return False

    return _check(result, operators_list=[], pos=0)


def get_total_calibration_result(lines):
    total = 0
    for line in lines:
        result, operands = parse_calibration_equation(line)
        if check_operands_combine_well(result, operands):
            total += result
    return total


def solve(input_path=None):
    if not input_path:
        aoc_root = Path(__file__).parents[3]
        input_path = aoc_root / "inputs" / "day_07" / "parts_1_2.txt"
    return get_total_calibration_result(get_lines(input_path))


if __name__ == "__main__":
    print("Day 07, Part 1:", solve())
