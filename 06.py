from utils import parse_input


puzzle_input = parse_input(day="06")[0]


def part_one():
    for i, _ in enumerate(puzzle_input):
        if len(set(puzzle_input[i-4:i])) == 4:
            return i


def part_two():
    for i, _ in enumerate(puzzle_input):
        if len(set(puzzle_input[i-14:i])) == 14:
            return i



if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
