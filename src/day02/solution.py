def part1(file_path):
    horizontal_position = 0
    depth_position = 0
    with open(file_path) as file:
        for line in file.readlines():
            command = line.split()[0]
            value = int(line.split()[1])
            if command == "up":
                depth_position -= value
            elif command == "down":
                depth_position += value
            elif command == "forward":
                horizontal_position += value
            else:
                print("Command unknown")
    return horizontal_position * depth_position


def part2(file_path):
    horizontal_position = 0
    depth_position = 0
    aim = 0
    with open(file_path) as file:
        for line in file.readlines():
            command = line.split()[0]
            value = int(line.split()[1])
            if command == "up":
                aim -= value
            elif command == "down":
                aim += value
            elif command == "forward":
                horizontal_position += value
                depth_position += aim * value
            else:
                print("Command unknown")
    return horizontal_position * depth_position


if __name__ == '__main__':
    print(part1("../../data/02-part1"))
    print(part2("../../data/02-part2"))
