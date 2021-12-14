from src.day14.solution import solve, solve_faster


def test_part1():
    steps = 10
    assert solve("../data/14-part1", steps) == 2223


def test_part2():
    steps = 40
    assert solve_faster("../data/14-part1", steps) == 2566282754493
