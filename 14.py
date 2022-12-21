from utils import parse_input

puzzle_input = parse_input(day="14")

goal_reached = False
coords = {}

min_x, min_y = [10**18 for _ in range(2)]
max_x, max_y = [-10**18 for _ in range(2)]

for line in puzzle_input:

    paths = [list(map(int, p.split(","))) for p in line.split(" -> ")]

    for i, _ in enumerate(paths[:-1]):
        
        s = paths[i]
        e = paths[i + 1]

        if s[0] < e[0]:
            x_r = range(s[0], e[0] + 1)
        else:
            x_r = range(s[0], e[0] - 1, -1)

        if s[1] < e[1]:
            y_r = range(s[1], e[1] + 1)
        else:
            y_r = range(s[1], e[1] - 1, -1)

        for x in x_r:

            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x

            for y in y_r:
                
                if y < min_y:
                    min_y = y
                elif y > max_y:
                    max_y = y

                coords[(x, y)] = "X"


def step(x, y, part):

    global goal_reached

    if part == 1:
        if y > max_y:
            goal_reached = True
            return

    elif part == 2:
        # Infinite wall at bottom.
        if y + 1 == max_y + 2:
            coords[(x, y)] = "o"
            return

    # Down
    if not (x, y + 1) in coords:
        step(x, y + 1, part)

    # Left
    elif not (x - 1, y + 1) in coords:
        step(x - 1, y + 1, part)
    
    # Right
    elif not (x + 1, y + 1) in coords:
        step(x + 1, y + 1, part)
    
    # Settled
    else:
        if part == 2:
            if (x, y) == (500, 0):
                goal_reached = True
        
        coords[(x, y)] = "o"
        

def part_one():
    
    grains = 0

    global goal_reached
    goal_reached = False
    
    while not goal_reached:
        step(500, 0, part=1)
        grains += 1
    
    return sum(1 for v in coords.values() if v == "o")


def part_two():

    grains = 0

    global goal_reached
    goal_reached = False

    while not goal_reached:
        step(500, 0, part=2)
        grains += 1

    return sum(1 for v in coords.values() if v == "o")


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    