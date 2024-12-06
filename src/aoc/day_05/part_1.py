# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from pathlib import Path

from aoc.common import get_lines
from aoc.day_05.dag import DAG


def get_sum_middle_pages(lines):
    dag = DAG()
    scan_mode = "rules"
    sum_middle_pages = 0
    for line in lines:
        if not line:
            scan_mode = "updates"
        elif scan_mode == "rules":
            before, after = map(int, line.split("|"))
            dag.add_edge(before, after)
        else:  # if mode == 'updates':
            pages = list(map(int, line.split(",")))
            is_valid_update = pages_sorted_correctly(dag, pages)
            if is_valid_update:
                sum_middle_pages += pages[len(pages) // 2]

    return sum_middle_pages


def pages_sorted_correctly(dag, pages):
    """Whether the pages are sorted correctly."""
    is_valid_update = True

    page_no = 0
    while is_valid_update and page_no < len(pages):
        page = pages[page_no]
        pages_after = pages[page_no + 1 :]
        pages_before = pages[:page_no]
        for page_after in pages_after:
            if not dag.edge_exists(page, page_after):
                is_valid_update = False
                break
        for page_before in pages_before:
            if not dag.edge_exists(page_before, page):
                is_valid_update = False
                break
        page_no += 1

    return is_valid_update


def solve(input_path=None):
    if not input_path:
        aoc_root = Path(__file__).parents[3]
        input_path = aoc_root / "inputs" / "day_05" / "parts_1_2.txt"
    return get_sum_middle_pages(get_lines(input_path))


if __name__ == "__main__":
    print("Day 05, Part 1:", solve())
