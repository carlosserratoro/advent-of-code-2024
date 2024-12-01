# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from collections import defaultdict
from pathlib import Path

from aoc.common import get_lines
from aoc.day_01.common import get_edge_numbers


def get_occurrences(lines):
    left_occurrences = defaultdict(int)
    right_occurrences = defaultdict(int)
    for line in lines:
        fields = get_edge_numbers(line)
        left_occurrences[fields[0]] += 1
        right_occurrences[fields[-1]] += 1
    return left_occurrences, right_occurrences


def get_similarity_score_from_occurrences(left_occurrences, right_occurrences):
    similarity_score = 0
    for left_number, left_occ in left_occurrences.items():
        similarity_score += (
            left_number * right_occurrences.get(left_number, 0)
        ) * left_occ
    return similarity_score


def get_similarity_score(lines):
    left_occurrences, right_occurrences = get_occurrences(lines)
    return get_similarity_score_from_occurrences(left_occurrences, right_occurrences)


def solve():
    aoc_root = Path(__file__).parents[3]
    input_path = aoc_root / "inputs" / "day_01" / "parts_1_2.txt"
    return get_similarity_score(get_lines(input_path))


if __name__ == "__main__":
    print("Day 01, Part 2:", solve())
