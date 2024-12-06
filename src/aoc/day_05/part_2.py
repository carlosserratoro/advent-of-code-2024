# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.common import get_lines
from aoc.day_05.dag import DAG
from aoc.day_05.part_1 import pages_sorted_correctly


def sort_pages(rules: DAG, pages: list):

    # Build a smaller DAG with only the rules that affect us.
    # This will speed up the search of the path.
    useful_rules = DAG()
    for i, page_i in enumerate(pages):
        for j, page_j in enumerate(pages):
            page_j = pages[j]
            if rules.edge_exists(page_i, page_j):
                useful_rules.add_edge(page_i, page_j)

    for i, page_i in enumerate(pages):
        for j, page_j in enumerate(pages):
            if i != j:
                paths = useful_rules.paths(
                    page_i,
                    page_j,
                    valid_nodes=set(pages),
                )
                for path in paths:
                    if path and set(path) == set(pages):
                        return path

    return False


def get_sum_middle_pages(lines):
    rules = DAG()
    updates_to_sort = []
    scan_mode = "rules"
    sum_middle_pages = 0
    for line in lines:
        if not line:
            scan_mode = "updates"
        elif scan_mode == "rules":
            before, after = map(int, line.split("|"))
            rules.add_edge(before, after)
        else:  # if mode == 'updates':
            pages = list(map(int, line.split(",")))
            if not pages_sorted_correctly(rules, pages):
                updates_to_sort.append(pages)

    for update_no, pages in enumerate(updates_to_sort):
        print(f"Sorting pages {update_no}/{len(updates_to_sort)} -> {pages}")
        sorted_pages = sort_pages(rules, pages)
        sum_middle_pages += sorted_pages[len(sorted_pages) // 2]

    return sum_middle_pages


def solve(input_path=None):
    if not input_path:
        aoc_root = Path(__file__).parents[3]
        input_path = aoc_root / "inputs" / "day_05" / "parts_1_2.txt"
    return get_sum_middle_pages(get_lines(input_path))


if __name__ == "__main__":
    print("Day 05, Part 2:", solve())
