# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence
import re

REGEX_EDGE_NUMBERS = re.compile(r"(\d+)\s+(\d+)")


def get_edge_numbers(line):
    """Given a line having numbers on each side, return them."""
    match = REGEX_EDGE_NUMBERS.search(line)
    return int(match.group(1)), int(match.group(2))
