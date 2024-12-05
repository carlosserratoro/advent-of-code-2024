# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.day_04.part_1 import solve, word_fits_in_position, yield_next_position


def test_yield_next_position():
    assert list(yield_next_position(start=(0, 0), direction="N", num_moves=2)) == [
        (0, 0),
        (-1, 0),
    ]
    assert list(yield_next_position(start=(0, 0), direction="NE", num_moves=2)) == [
        (0, 0),
        (-1, 1),
    ]
    assert list(yield_next_position(start=(0, 0), direction="E", num_moves=2)) == [
        (0, 0),
        (0, 1),
    ]
    assert list(yield_next_position(start=(0, 0), direction="SE", num_moves=2)) == [
        (0, 0),
        (1, 1),
    ]
    assert list(yield_next_position(start=(0, 0), direction="S", num_moves=2)) == [
        (0, 0),
        (1, 0),
    ]
    assert list(yield_next_position(start=(0, 0), direction="SW", num_moves=2)) == [
        (0, 0),
        (1, -1),
    ]
    assert list(yield_next_position(start=(0, 0), direction="W", num_moves=2)) == [
        (0, 0),
        (0, -1),
    ]
    assert list(yield_next_position(start=(0, 0), direction="NW", num_moves=2)) == [
        (0, 0),
        (-1, -1),
    ]


def test_word_fits_in_position():
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert word_fits_in_position(matrix, (0, 0), "E", "Hi") is True
    assert word_fits_in_position(matrix, (0, 1), "E", "Hi") is True
    assert word_fits_in_position(matrix, (0, 2), "E", "Hi") is False
    assert word_fits_in_position(matrix, (1, 0), "E", "Hi") is True
    assert word_fits_in_position(matrix, (1, 1), "E", "Hi") is True
    assert word_fits_in_position(matrix, (1, 2), "E", "Hi") is False


def test_solve():
    assert 2603 == solve()


def test_solve_test():
    aoc_root = Path(__file__).parents[2]
    test_input_path = aoc_root / "inputs" / "day_04" / "parts_1_2_test.txt"
    assert 18 == solve(test_input_path)
