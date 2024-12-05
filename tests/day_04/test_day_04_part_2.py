# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.day_04.part_2 import (
    crossed_mas_found,
    get_translated_position,
    position_can_contain_crossed_mas,
    solve,
)


def test_crossed_mas_found():
    assert (
        crossed_mas_found([["M", "?", "S"], ["?", "A", "?"], ["M", "?", "S"]], (1, 1))
        is True
    )
    assert (
        crossed_mas_found([["?", "?", "S"], ["?", "A", "?"], ["M", "?", "S"]], (1, 1))
        is False
    )


def test_get_translated_position():
    assert get_translated_position((0, 0), "ne") == (-1, 1)
    assert get_translated_position((0, 0), "se") == (1, 1)
    assert get_translated_position((0, 0), "nw") == (-1, -1)
    assert get_translated_position((0, 0), "sw") == (1, -1)


def test_position_can_contain_crossed_mas():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert position_can_contain_crossed_mas(matrix, (1, 1)) is True
    for row in range(3):
        for col in range(3):
            pos = row, col
            if pos != (1, 1):
                assert position_can_contain_crossed_mas(matrix, pos) is False


def test_solve():
    assert 1965 == solve()


def test_solve_test():
    aoc_root = Path(__file__).parents[2]
    test_input_path = aoc_root / "inputs" / "day_04" / "parts_1_2_test.txt"
    assert 9 == solve(test_input_path)
