def is_unique(map_entry):
    if len(map_entry) == 1:
        return True
    else:
        return False


def part1(file_path):
    mapping = {
        2: [1],
        3: [7],
        4: [4],
        5: [2, 3, 5],
        6: [0, 6, 9],
        7: [8]
    }
    with open(file_path) as file:
        counter = 0
        for line in file.readlines():
            l1 = line.split("|")[1].strip().split(" ")
            for signal in l1:
                signal_len = len([c for c in signal])
                if is_unique(mapping[signal_len]):
                    counter += 1
    return counter


if __name__ == '__main__':
    print(part1("../../data/08-test"))
    # mapping = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
