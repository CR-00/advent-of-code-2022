from utils import parse_input


puzzle_input = parse_input(day="05")


def make_columns():
    columns = [[], [], [], [], [], [], [], [], []]
    for line in puzzle_input[:8]:
        for i in range(1, 34, 4):
            if len(line) > i and line[i] != " ":
                columns[i // 4].append(line[i])

    return [list(reversed(c)) for c in columns]


def part_one():

    columns = make_columns()

    for instruction in puzzle_input[10:]:
    
        _, number, _, src, _, dst = list(instruction.split(" "))
    
        number, src, dst = int(number), int(src) - 1, int(dst) - 1

        columns[dst] += reversed(columns[src][-number:])

        columns[src] = columns[src][:-number]
    
    return "".join([c[-1] for c in columns])


def part_two():

    columns = make_columns()

    for instruction in puzzle_input[10:]:

        _, number, _, src, _, dst = list(instruction.split(" "))

        number, src, dst = int(number), int(src) - 1, int(dst) - 1

        columns[dst] += columns[src][-number:]

        columns[src] = columns[src][:-number]
    
    return "".join([c[-1] for c in columns])



if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
