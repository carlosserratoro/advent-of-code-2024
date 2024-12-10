# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.common import get_lines


def parse_calibration_equation(line):
    fields = line.split()
    result = int(fields[0].rstrip(":"))
    operands = list(map(int, fields[1:]))
    return result, operands


def apply(operands, operators_list, allowed_operators, result=None):
    """Apply the operators in between the operands, left-to-right order.

    This is a Polish notation if we reverse the operators and put them
    before the operands and then we evaluate it normally.

    Returns -1 if solution is not feasible, another number >0 otherwise.
    """
    # Example: If operands were 3, 2, 7, and operands were + *
    # then in Polish notation it would be * + 3 2 7 for (3 + 2) * 7:
    # To allow for a fast prune, we are going to allow for partial evaluation,
    # meaning that we'll receive the full list of operands, e.g. 3, 2, 7, but
    # maybe not all the operands (in this example we'd need two operands, but
    # we may receive just one), e.g. +. Then, we'd evaluate just + 3 2
    polish = list(reversed(operators_list)) + operands[: len(operators_list) + 1]
    stack = []
    for elem in reversed(polish):
        if elem in allowed_operators:
            res = allowed_operators[elem](stack)
            if result and res > result:
                return -1
            stack.append(res)
        else:
            stack.append(elem)
    return stack.pop() if stack else -1


def check_operands_combine_well(result, operands, allowed_operators):
    """Check if the operands can yield the result if properly combined."""

    def _check(result, operators_list, pos):
        res = apply(operands, operators_list, allowed_operators, result)
        if res > result:
            return False
        if pos == len(operands) - 1:
            return res == result
        for op in allowed_operators:
            operators_list.append(op)
            if _check(result, operators_list, pos + 1):
                return True
            operators_list.pop()
        return False

    return _check(result, operators_list=[], pos=0)


def get_total_calibration_result(lines, allowed_operators):
    total = 0
    for line in lines:
        result, operands = parse_calibration_equation(line)
        if check_operands_combine_well(result, operands, allowed_operators):
            total += result
    return total


def solve(allowed_operators, input_path=None):
    if not input_path:
        aoc_root = Path(__file__).parents[3]
        input_path = aoc_root / "inputs" / "day_07" / "parts_1_2.txt"
    return get_total_calibration_result(get_lines(input_path), allowed_operators)
