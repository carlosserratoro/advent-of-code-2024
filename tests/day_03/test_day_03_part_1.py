# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_03.common import get_mul_operands
from aoc.day_03.part_1 import get_mul, solve


def test_get_mul_operands():
    assert (1, 2) == get_mul_operands("mul(1,2)")
    assert (11, 22) == get_mul_operands("mul(11,22)")
    assert (111, 222) == get_mul_operands("mul(111,222)")


def test_get_mul():
    assert ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"] == list(
        get_mul(
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
    )


def test_solve():
    assert 184511516 == solve()
