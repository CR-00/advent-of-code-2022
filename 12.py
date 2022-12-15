from utils import parse_input
from collections import deque


puzzle_input = parse_input(day="12")


for i, line in enumerate(puzzle_input):
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
            puzzle_input[i] = puzzle_input[i][:j] + "a" + puzzle_input[i][j+1:]
        if c == "E":
            end = (i, j)
            puzzle_input[i] = puzzle_input[i][:j] + "z" + puzzle_input[i][j+1:]


def neighbours(i, j):
    ret = []
    if i > 0:
        ret.append((i - 1, j))
    if i < len(puzzle_input) - 1:
        ret.append((i + 1, j))
    if j > 0:
        ret.append((i, j - 1))
    if j < len(puzzle_input[0]) - 1:
        ret.append((i, j + 1))
    return ret


def part_one():

    q = deque([(start, 0)])
    costs = {}

    while len(q):

        (x, y), c = q.popleft()
        
        for (i, j) in neighbours(x, y):
            if not (i, j) in costs:
                if ord(puzzle_input[i][j]) <= ord(puzzle_input[x][y]) + 1:
                    q.append(((i, j), c + 1))
                    costs[(i, j)] = c + 1

    return costs[end]


def part_two():

    starts = []
    for i, line in enumerate(puzzle_input):
        for j, c in enumerate(line):
            if puzzle_input[i][j] == "a":
                starts.append((i, j))

    q = deque([(s, 0) for s in starts])
    costs = {}

    while len(q):

        (x, y), c = q.popleft()
        
        for (i, j) in neighbours(x, y):
            if not (i, j) in costs:
                if ord(puzzle_input[i][j]) <= ord(puzzle_input[x][y]) + 1:
                    q.append(((i, j), c + 1))
                    costs[(i, j)] = c + 1
            
    return costs[end]


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    