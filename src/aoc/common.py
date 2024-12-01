# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence


def get_lines(file_path):
    """Yield the lines of a file."""
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip()
