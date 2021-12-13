syntax_error_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
tags = {"(": ")", "[": "]", "<": ">", "{": "}"}


def part1(file_path):
    error_score = 0
    with open(file_path) as file:
        for x in file.readlines():
            l = x.strip()
            stack = []
            for a in l:
                if a in tags:
                    stack.append(a)
                else:
                    p = stack.pop()
                    if a != tags[p]:
                        error_score += syntax_error_points[a]
            if len(stack) != 0:
                print(x)
    return error_score


if __name__ == '__main__':
    print(part1("../../data/10-part1"))
