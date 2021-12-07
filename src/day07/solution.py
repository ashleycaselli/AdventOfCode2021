import sys


def part1(file_path):
    with open(file_path) as file:
        positions = [int(x) for x in file.read().split(",")]
        lower_bound = min(positions)
        upper_bound = max(positions)
        fuel_cost = sys.maxsize
        for index in range(lower_bound, upper_bound):
            fuel = 0
            for pos in positions:
                fuel += abs(pos - index)
            if fuel < fuel_cost:
                fuel_cost = fuel
    return fuel_cost


def part2(file_path):
    with open(file_path) as file:
        positions = [int(x) for x in file.read().split(",")]
        lower_bound = min(positions)
        upper_bound = max(positions)
        fuel_cost = sys.maxsize
        for index in range(lower_bound, upper_bound):
            fuel = 0
            for pos in positions:
                counter_limit = abs(pos - index)
                total = [x for x in range(1, counter_limit + 1)]
                total_sum = sum(total)
                fuel += total_sum
            if fuel < fuel_cost:
                fuel_cost = fuel
    return fuel_cost


if __name__ == '__main__':
    print(part1("../../data/07-part1"))
    print(part2("../../data/07-part2"))
