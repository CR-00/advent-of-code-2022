from utils import parse_input


puzzle_input = [i.split(",") for i in parse_input(day="04")]


def part_one():

    strict_subsets = 0

    for first_pair, second_pair in puzzle_input:
        
        f = list(map(int, first_pair.split("-")))
        s = list(map(int, second_pair.split("-")))

        f = set(range(f[0], f[-1] + 1))
        s = set(range(s[0], s[-1] + 1))

        if f.issuperset(s) or s.issuperset(f):
            strict_subsets += 1
    
    return strict_subsets


def part_two():

    intersects = 0

    for first_pair, second_pair in puzzle_input:
        
        f = list(map(int, first_pair.split("-")))
        s = list(map(int, second_pair.split("-")))

        f = set(range(f[0], f[-1] + 1))
        s = set(range(s[0], s[-1] + 1))

        if s & f:
            intersects += 1

    return intersects


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
