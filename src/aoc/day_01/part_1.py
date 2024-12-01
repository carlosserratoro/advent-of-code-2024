# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.common import get_lines
from aoc.day_01.common import get_edge_numbers


def get_location_lists(location_lines):
    left_list = []
    right_list = []
    for line in location_lines:
        locations = get_edge_numbers(line)
        left_list.append(locations[0])
        right_list.append(locations[1])
    return left_list, right_list


def get_total_distance_between_lists(left_list, right_list):
    left_list.sort()
    right_list.sort()
    sum_total_distance = 0
    for item_no, item_left in enumerate(left_list):
        item_right = right_list[item_no]
        sum_total_distance += abs(item_left - item_right)
    return sum_total_distance


def get_total_distance(location_lines):
    left_list, right_list = get_location_lists(location_lines)
    return get_total_distance_between_lists(left_list, right_list)


def solve():
    aoc_root = Path(__file__).parents[3]
    input_path = aoc_root / "inputs" / "day_01" / "parts_1_2.txt"
    return get_total_distance(get_lines(input_path))


if __name__ == "__main__":
    print("Day 01, Part 1:", solve())
