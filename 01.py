import operator

data = []

with open("./inputs/01-part-one.txt", "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


def part_one():
    return max(enumerate([sum(list(map(int, j))) for j in [i.split(",") for i in ",".join(data).split(",,")]]), key=operator.itemgetter(1))[1]

def part_two():
    return sum(sorted([sum(list(map(int, j))) for j in [i.split(",") for i in ",".join(data).split(",,")]], reverse=True)[:3])


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")