def get_adjacent(hmap, i, k):
    adj = []
    if i - 1 >= 0:
        adj.append(hmap[i - 1][k])
    if i + 1 < len(hmap):
        adj.append(hmap[i + 1][k])
    if k - 1 >= 0:
        adj.append(hmap[i][k - 1])
    if k + 1 < len(hmap[i]):
        adj.append(hmap[i][k + 1])
    return adj


def get_adjacent_with_index(hmap, i, k):
    adj = []
    if i - 1 >= 0:
        adj.append((hmap[i - 1][k], i - 1, k))
    if i + 1 < len(hmap):
        adj.append((hmap[i + 1][k], i + 1, k))
    if k - 1 >= 0:
        adj.append((hmap[i][k - 1], i, k - 1))
    if k + 1 < len(hmap[i]):
        adj.append((hmap[i][k + 1], i, k + 1))
    return adj


def part1(file_path):
    with open(file_path) as file:
        heightmap = [[int(x) for x in y.strip()] for y in file.readlines()]
        low_points = []
        for i in range(0, len(heightmap)):
            for k in range(0, len(heightmap[i])):
                val = heightmap[i][k]
                if val < min(get_adjacent(heightmap, i, k)):
                    low_points.append(val)
    return sum(low_points) + len(low_points)


def basin(hmap, point):
    r = set()
    adj = get_adjacent_with_index(hmap, point[1], point[2])
    for a in adj:
        if a[0] > point[0] and a[0] != 9:
            r.add(a)
            r.update(basin(hmap, a))
    return r


def part2(file_path):
    with open(file_path) as file:
        heightmap = [[int(x) for x in y.strip()] for y in file.readlines()]
        low_points = []
        for i in range(0, len(heightmap)):
            for k in range(0, len(heightmap[i])):
                val = heightmap[i][k]
                if val < min(get_adjacent(heightmap, i, k)):
                    low_points.append((val, i, k))
    basins = []
    for low in low_points:
        b = basin(heightmap, low)
        b.add(low)
        basins.append(b)

    basins.sort(key=len)
    res = 1
    for i in range(0, 3):
        res *= len(basins[len(basins) - i - 1])
    return res


if __name__ == '__main__':
    print(part1("../../data/09-part1"))
    print(part2("../../data/09-part2"))
