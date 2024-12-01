# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_01.common import get_edge_numbers


def test_parse_locations():
    assert (123, 456) == get_edge_numbers("123     456")
