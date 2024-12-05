# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence


def get_lines(file_path):
    """Yield the lines of a file."""
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip()


def yield_matrix_positions(matrix):
    """Generate a stream of positions (row, column) from a matrix."""
    num_rows, num_cols = len(matrix), len(matrix[0])
    for num_row in range(num_rows):
        for num_col in range(num_cols):
            yield num_row, num_col
