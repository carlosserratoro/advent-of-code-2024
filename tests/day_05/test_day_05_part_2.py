# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.day_05.part_2 import solve


def test_solve():
    assert 6004 == solve()


def test_solve_test():
    aoc_root = Path(__file__).parents[2]
    test_input_path = aoc_root / "inputs" / "day_05" / "parts_1_2_test.txt"
    assert 123 == solve(test_input_path)
