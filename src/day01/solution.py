def part1(file_path):
    with open(file_path) as file:
        lines = [int(x.replace("\n", "")) for x in file.readlines()]
        increments = 0
        previous_value = lines[0]
        for current_value in lines[1:]:
            if current_value > previous_value:
                increments += 1
            previous_value = current_value
    return increments


def part2(file_path):
    with open(file_path) as file:
        lines = [int(x.replace("\n", "")) for x in file.readlines()]
        increments = 0
        previous_sum = 0
        for index in range(0, len(lines)):
            current_sum = sum(lines[index: index + 3])
            if current_sum > previous_sum:
                increments += 1
            previous_sum = current_sum
            if (index + 3) == (len(lines) - 1):
                break
    return increments


if __name__ == '__main__':
    print(part1("../../data/01-part1"))
    print(part2("../../data/01-part2"))
