from src.day01.solution import part1, part2
import os

def test_part1():
    print(os.pwd())
    assert part1("../data/01-part1") == 1766


def test_part2():
    assert part2("../data/01-part2") == 1797
