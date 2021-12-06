def part1(file_path):
    gamma_rate_bin = "0b"
    epsilon_rate_bin = "0b"
    with open(file_path) as file:
        lines = file.readlines()
        line_char = [[int(x) for x in line.strip()] for line in lines]
        col_number = len(line_char[0])
        for index in range(0, col_number):
            count = {0: 0, 1: 0}
            for x in line_char:
                count[x[index]] += 1
            most_common = max(count.items(), key=lambda x: x[1])[0]
            less_common = min(count.items(), key=lambda x: x[1])[0]
            gamma_rate_bin += str(most_common)
            epsilon_rate_bin += str(less_common)
    return int(gamma_rate_bin, 2) * int(epsilon_rate_bin, 2)


def part2(file_path):
    o2_rating = "0b"
    co2_rating = "0b"
    with open(file_path) as file:
        lines = file.readlines()
        line_char = [[int(x) for x in line.strip()] for line in lines]
        col_number = len(line_char[0])

        keep_most = line_char
        keep_less = line_char

        for index in range(0, col_number):
            count = {0: 0, 1: 0}
            for x in keep_most:
                count[x[index]] += 1
            most_common = max(count.items(), key=lambda x: x[1])[0] if count[0] != count[1] else 1
            keep_most = list(filter(lambda x: x[index] == most_common, keep_most))
            if len(keep_most) == 1:
                break

        for index in range(0, col_number):
            count = {0: 0, 1: 0}
            for x in keep_less:
                count[x[index]] += 1
            less_common = min(count.items(), key=lambda x: x[1])[0] if count[0] != count[1] else 0
            keep_less = list(filter(lambda x: x[index] == less_common, keep_less))
            if len(keep_less) == 1:
                break

        o2_rating += "".join(map(str, keep_most[0]))
        co2_rating += "".join(map(str, keep_less[0]))

        return int(o2_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
    print(part1("../../data/03-part1"))
    print(part2("../../data/03-part2"))
