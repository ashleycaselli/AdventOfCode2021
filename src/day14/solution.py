import collections

STEPS_PART1 = 10
STEPS_PART2 = 40


def solve(file_path, steps):
    with open(file_path) as file:
        lines = [x.strip() for x in file.readlines()]
        template = lines[0]
        rules = {}

        for x in lines[2:]:
            r = x.split("->")
            rules[r[0].strip()] = r[1].strip()

        for _ in range(steps):
            res = template[0]
            for i in range(len(template) - 1):
                res += rules[template[i] + template[i + 1]] + template[i + 1]

            template = res
        count = collections.Counter(res).most_common()
        return count[0][1] - count[len(count) - 1][1]


def solve_faster(file_path, steps):
    with open(file_path) as file:
        lines = [x.strip() for x in file.readlines()]
        template = lines[0]
        rules = {}

        for x in lines[2:]:
            r = x.split("->")
            rules[r[0].strip()] = r[1].strip()

        pairs = {}
        for j in range(len(template) - 1):
            pair = template[j] + template[j + 1]
            pairs[pair] = pairs.get(pair, 0) + 1

        for i in range(steps):
            new_pairs = {}
            for pk, pv in pairs.items():
                pair = pk[0] + rules[pk]
                new_pairs[pair] = new_pairs.get(pair, 0) + pv
                pair = rules[pk] + pk[1]
                new_pairs[pair] = new_pairs.get(pair, 0) + pv
            pairs = new_pairs.copy()

        counts = {}
        for k, v in pairs.items():
            counts[k[0]] = counts.get(k[0], 0) + v

        counts[template[len(template) - 1]] = counts[template[len(template) - 1]] + 1

        char_count = collections.Counter(counts).most_common()
        return char_count[0][1] - char_count[len(char_count) - 1][1]


if __name__ == '__main__':
    print(solve("../../data/14-part1", STEPS_PART1))
    print(solve_faster("../../data/14-part1", STEPS_PART2))
