from utils import parse_input
from collections import defaultdict


puzzle_input = parse_input(day="07")


def part_one():

    du = defaultdict(int)
    path = ["/"]

    for line in puzzle_input[1:]:
        if "$ cd" in line:
            directory = line.split()[2]
            if directory == "..":
                path.pop()
            else:
                path.append(f"{path[-1]}/{directory}")
        if not "dir" in line and not "$" in line:
            for dir_ in path:
                du[dir_] += int(line.split()[0])

    total_du = 0
    for v in du.values():
        if v <= 100000:
            total_du += v
    return total_du


def part_two():

    du = defaultdict(int)
    path = ["/"]

    for line in puzzle_input[1:]:
        if "$ cd" in line:
            directory = line.split()[2]
            if directory == "..":
                path.pop()
            else:
                path.append(f"{path[-1]}/{directory}")
        if not "dir" in line and not "$" in line:
            for dir_ in path:
                du[dir_] += int(line.split()[0])

    deletion_candidates = []
    for v in du.values():
        if v >= 30000000 - (70000000 - du['/']):
            deletion_candidates.append(v)

    return min(deletion_candidates)


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
