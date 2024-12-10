# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence
from pathlib import Path

import pytest

from aoc.day_07.part_2 import get_ops, solve


def test_solve_test():
    aoc_root = Path(__file__).parents[2]
    test_input_path = aoc_root / "inputs" / "day_07" / "parts_1_2_test.txt"
    assert 11387 == solve(get_ops(), test_input_path)


@pytest.mark.solution
def test_solve():
    assert 275791737999003 == solve(get_ops())
