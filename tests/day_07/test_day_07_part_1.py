# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

import pytest

from aoc.day_07.part_1 import get_ops, solve


def test_solve():
    assert 1399219271639 == solve(get_ops())


@pytest.mark.solution
def test_solve_test():
    aoc_root = Path(__file__).parents[2]
    test_input_path = aoc_root / "inputs" / "day_07" / "parts_1_2_test.txt"
    assert 3749 == solve(get_ops(), test_input_path)
