import operator
from utils import parse_input


puzzle_input = parse_input(day="01")


def part_one():
    return max(enumerate([sum(list(map(int, j))) for j in [i.split(",") for i in ",".join(puzzle_input).split(",,")]]), key=operator.itemgetter(1))[1]


def part_two():
    return sum(sorted([sum(list(map(int, j))) for j in [i.split(",") for i in ",".join(puzzle_input).split(",,")]], reverse=True)[:3])


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")