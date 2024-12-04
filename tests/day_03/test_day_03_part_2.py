# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_03.part_2 import (
    I_DO,
    I_DONT,
    I_MUL,
    get_added_mul,
    get_instructions,
    solve,
)


def test_get_instructions():
    assert list(
        get_instructions(
            "xmul(2,4)!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
    ) == [
        (I_MUL, "mul(2,4)"),
        (I_DONT, None),
        (I_MUL, "mul(5,5)"),
        (I_MUL, "mul(11,8)"),
        (I_DO, None),
        (I_MUL, "mul(8,5)"),
    ]


def test_get_added_mul():
    assert (
        get_added_mul(
            ["xmul(2,4)!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
        )
        == 48
    )


def test_solve():
    assert 90044227 == solve()
