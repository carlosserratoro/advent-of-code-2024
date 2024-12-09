# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.day_07.part_1 import (
    apply,
    check_operands_combine_well,
    parse_calibration_equation,
    solve,
)


def test_apply():
    assert apply([2, 3], ["+"]) == 5
    assert apply([2, 3, 4], ["+", "*"]) == 20


def test_check_operands_combine_well():
    assert check_operands_combine_well(190, [19, 10]) is True
    assert check_operands_combine_well(83, [17, 5]) is False
    assert check_operands_combine_well(3267, [81, 40, 27]) is True
    assert check_operands_combine_well(7290, [6, 8, 6, 15]) is False


def test_parse_calibration_equation():
    assert parse_calibration_equation("5: 2 3") == (5, [2, 3])


def test_solve():
    assert 1399219271639 == solve()


def test_solve_test():
    aoc_root = Path(__file__).parents[2]
    test_input_path = aoc_root / "inputs" / "day_07" / "parts_1_2_test.txt"
    assert 3749 == solve(test_input_path)
