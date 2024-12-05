# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence
from pathlib import Path

from aoc.common import get_lines, yield_matrix_positions


def get_translated_position(position, direction):
    assert direction in ("ne", "nw", "se", "sw")
    offset = (
        1 if "s" in direction else -1,
        1 if "e" in direction else -1,
    )
    return position[0] + offset[0], position[1] + offset[1]


def position_can_contain_crossed_mas(matrix, center_pos):
    """Whether a crossed MAS can be centered at the position."""
    row, col = center_pos
    num_rows, num_cols = len(matrix), len(matrix[0])
    for offset in (-1, +1):
        if (
            row + offset < 0
            or row + offset >= num_rows
            or col + offset < 0
            or col + offset >= num_cols
        ):
            return False
    return True


def crossed_mas_found(matrix, center_pos):
    """Whether there is a MAS centered in the position."""
    matrix_ne_pos = get_translated_position(center_pos, "ne")
    matrix_nw_pos = get_translated_position(center_pos, "nw")
    matrix_se_pos = get_translated_position(center_pos, "se")
    matrix_sw_pos = get_translated_position(center_pos, "sw")
    matrix_ne = matrix[matrix_ne_pos[0]][matrix_ne_pos[1]]
    matrix_nw = matrix[matrix_nw_pos[0]][matrix_nw_pos[1]]
    matrix_se = matrix[matrix_se_pos[0]][matrix_se_pos[1]]
    matrix_sw = matrix[matrix_sw_pos[0]][matrix_sw_pos[1]]
    matrix_center = matrix[center_pos[0]][center_pos[1]]
    return (
        matrix_center == "A"
        and (
            matrix_nw == "M"
            and matrix_se == "S"
            or matrix_nw == "S"
            and matrix_se == "M"
        )
        and (
            matrix_ne == "M"
            and matrix_sw == "S"
            or matrix_ne == "S"
            and matrix_sw == "M"
        )
    )


def get_num_crossed_mas(lines):
    num_crossed_mas = 0

    # Build the matrix for the word search.
    matrix = []
    for line in lines:
        matrix.append(line)

    for center_pos in yield_matrix_positions(matrix):
        if position_can_contain_crossed_mas(matrix, center_pos):
            if crossed_mas_found(matrix, center_pos):
                num_crossed_mas += 1

    return num_crossed_mas


def solve(input_path=None):
    if not input_path:
        aoc_root = Path(__file__).parents[3]
        input_path = aoc_root / "inputs" / "day_04" / "parts_1_2.txt"
    return get_num_crossed_mas(get_lines(input_path))


if __name__ == "__main__":
    print("Day 04, Part 2:", solve())
