# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence
from functools import lru_cache
from pathlib import Path

from aoc.common import get_lines

# The directions in which we can move: cardinal points.
DIRECTIONS = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]


def yield_positions(matrix):
    """Generate a stream of positions (row, column) from a matrix."""
    num_rows, num_cols = len(matrix), len(matrix[0])
    for num_row in range(num_rows):
        for num_col in range(num_cols):
            yield num_row, num_col


@lru_cache(maxsize=len(DIRECTIONS))
def give_step_vector(direction):
    """Get step vector given direction and orientation."""
    step_col = 1 if "E" in direction else -1 if "W" in direction else 0
    step_row = -1 if "N" in direction else 1 if "S" in direction else 0
    return step_row, step_col


def word_fits_in_position(matrix, start, direction, word):
    """Whether the word fits in the matrix given the position and direction."""
    step_row, step_col = give_step_vector(direction)
    final_row = start[0] + ((len(word) - 1) * step_row)
    final_col = start[1] + ((len(word) - 1) * step_col)
    return 0 <= final_row < len(matrix) and 0 <= final_col < len(matrix[0])


def yield_next_position(start, direction, num_moves):
    """Yield positions to traverse given a starting point and direction."""
    step_row, step_col = give_step_vector(direction)
    row, col = start
    for _ in range(num_moves):
        yield row, col
        row += step_row
        col += step_col


def word_found(matrix, start, direction, word):
    """Count how many times the word is inside the matrix."""
    if has_word := word_fits_in_position(matrix, start, direction, word):
        for position_no, position in enumerate(
            yield_next_position(start, direction, num_moves=len(word))
        ):
            row = position[0]
            col = position[1]
            if word[position_no] != matrix[row][col]:
                has_word = False
                break
    return has_word


def get_num_words(lines, word):
    num_words = 0

    # Build the matrix for the word search.
    matrix = []
    for line in lines:
        matrix.append(line)

    for start in yield_positions(matrix):
        for direction in DIRECTIONS:
            if word_found(matrix, start, direction, word):
                num_words += 1

    return num_words


def solve(input_path=None):
    if not input_path:
        aoc_root = Path(__file__).parents[3]
        input_path = aoc_root / "inputs" / "day_04" / "parts_1_2.txt"
    return get_num_words(get_lines(input_path), word="XMAS")


if __name__ == "__main__":
    print("Day 04, Part 1:", solve())
