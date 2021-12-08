def part1(file_path):
    with open(file_path) as file:
        lines = [[int(x) for x in y.strip().replace("->", ",").split(",")] for y in file.readlines()]
        coverage = {}
        for line in lines:
            start_point = {"x": line[0], "y": line[1]}
            end_point = {"x": line[2], "y": line[3]}
            if start_point["x"] == end_point["x"]:
                upper = max(start_point["y"], end_point["y"])
                lower = min(start_point["y"], end_point["y"])
                for i in range(lower, upper + 1):
                    if (start_point["x"], i) not in coverage:
                        coverage[start_point["x"], i] = 0
                    coverage[start_point["x"], i] += 1
            if start_point["y"] == end_point["y"]:
                upper = max(start_point["x"], end_point["x"])
                lower = min(start_point["x"], end_point["x"])
                for i in range(lower, upper + 1):
                    if (i, start_point["y"]) not in coverage:
                        coverage[i, start_point["y"]] = 0
                    coverage[i, start_point["y"]] += 1
        return len([k for k, v in coverage.items() if v > 1])


def part2(file_path):
    return None


if __name__ == '__main__':
    print(part1("../../data/05-part1"))
    print(part2("../../data/05-part2"))
