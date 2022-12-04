import string
from utils import parse_input


puzzle_input = parse_input(day="03")


character_priorities = list(
    string.ascii_lowercase +
    string.ascii_uppercase
)


def part_one():

    total = 0

    for rucksack in puzzle_input:
        
        # Get whats common across both halves.
        shared_item = (
            set(rucksack[:len(rucksack) // 2]) &
            set(rucksack[len(rucksack) // 2:])
        )

        # Priority is index in concatenated alphabets plus one.
        total += character_priorities.index(shared_item.pop()) + 1
        
    return total


def part_two():

    total = 0

    for i in range(0, len(puzzle_input), 3):

        one, two, three = puzzle_input[i: i + 3]

        badge = set(one) & set(two) & set(three)
        
        total += character_priorities.index(badge.pop()) + 1

    return total


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")