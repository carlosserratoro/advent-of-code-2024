# Authored by Carlos Serra-Toro (https://carlosserratoro.com)
# See the file LICENSE for the licence

from aoc.day_07.common import solve


def get_ops():
    return {
        "+": lambda stack: stack.pop() + stack.pop(),
        "*": lambda stack: stack.pop() * stack.pop(),
        "|": lambda stack: int("".join([str(stack.pop()), str(stack.pop())])),
    }


if __name__ == "__main__":
    print("Day 07, Part 2:", solve(allowed_operators=get_ops()))
