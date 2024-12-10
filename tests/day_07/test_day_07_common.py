# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence


from aoc.day_07.common import (
    apply,
    check_operands_combine_well,
    parse_calibration_equation,
)
from aoc.day_07.part_1 import get_ops

OPS = get_ops()


def test_apply():
    assert apply([2, 3], ["+"], OPS) == 5
    assert apply([2, 3, 4], ["+", "*"], OPS) == 20


def test_check_operands_combine_well():
    assert check_operands_combine_well(190, [19, 10], OPS) is True
    assert check_operands_combine_well(83, [17, 5], OPS) is False
    assert check_operands_combine_well(3267, [81, 40, 27], OPS) is True
    assert check_operands_combine_well(7290, [6, 8, 6, 15], OPS) is False


def test_parse_calibration_equation():
    assert parse_calibration_equation("5: 2 3") == (5, [2, 3])
