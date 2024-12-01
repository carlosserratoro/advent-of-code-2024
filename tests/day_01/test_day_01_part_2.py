# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_01.part_2 import get_similarity_score_from_occurrences, solve


def test_get_similarity_score_from_occurrences():
    assert 31 == get_similarity_score_from_occurrences(
        {3: 3, 4: 1, 2: 1, 1: 1}, {3: 3, 4: 1, 5: 1, 9: 1}
    )


def test_solve():
    assert 22565391 == solve()
