# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_01.part_1 import get_total_distance_between_lists, solve


def test_get_total_distance_between_lists():
    assert 11 == get_total_distance_between_lists(
        [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]
    )


def test_solution():
    assert 3574690 == solve()
