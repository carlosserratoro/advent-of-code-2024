# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.common import get_lines
from aoc.day_05.dag import DAG
from aoc.day_05.part_1 import pages_sorted_correctly


def sort_pages(rules: DAG, pages: list):
    """Sort the pages according to the rules given."""

    # Build a smaller DAG with only the rules that affect us.
    # Due to the wording of the problem limiting the order to be
    # defined by explicit rules (i.e. edges in our case), we can
    # filter out all the others, being sure no indirect order can
    # be obtained from them (not because it's not possible, but
    # because  the problem limits it on purpose). This allows us
    # to use a topological sorting with the guarantee that it'll
    # be unique, which allows us to get the sorted sequence.
    useful_rules = DAG()
    for page_i in pages:
        for page_j in pages:
            if rules.edge_exists(page_i, page_j):
                useful_rules.add_edge(page_i, page_j)
    return useful_rules.topsort()


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
