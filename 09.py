from utils import parse_input

puzzle_input = parse_input(day="09")


def move(rope, direction):
    if direction == "U":
        rope[1] += 1
    elif direction == "D":
        rope[1] -= 1
    elif direction == "L":
        rope[0] -= 1
    elif direction == "R":
        rope[0] += 1


def part_one():

    visited = []

    head, tail = [0, 0], [0, 0]

    for line in puzzle_input:
    
        direction, distance = line[0], int(line[1:])
        
        for _ in range(distance):

            move(head, direction)

            x_dist = head[0] - tail[0]
            y_dist = head[1] - tail[1]

            if abs(x_dist) >= 2 or abs(y_dist) >= 2:

                # Is up or down.
                if head[1] == tail[1]:
                    move(tail, direction)

                # Is left or right.
                elif head[0] == tail[0]:
                    move(tail, direction)
                
                # Is diagonal.
                else:
                    if x_dist > 0:
                        move(tail, "R")
                    else:
                        move(tail, "L")
                    
                    if y_dist > 0:
                        move(tail, "U")
                    else:
                        move(tail, "D")

                visited.append(tuple(tail))

    return len(set(visited))


def part_two():

    visited = [(0, 0)]

    knots = [[0, 0] for _ in range(10)]

    for line in puzzle_input:
        
        direction, distance = line[0], int(line[1:])
        
        for _ in range(distance):

            # Move the head forward.
            move(knots[0], direction)
            
            for i in range(9):
                
                # Move the tail back in the line.
                head = knots[i]
                tail = knots[i + 1]

                x_dist = head[0] - tail[0]
                y_dist = head[1] - tail[1]

                if abs(x_dist) >= 2 or abs(y_dist) >= 2:

                    # Move up or down.
                    if x_dist == 0:
                        tail[1] += y_dist // 2
                    
                    # Move left or right.
                    elif y_dist == 0:
                        tail[0] += x_dist // 2

                    # Move diagonally.
                    else:
                        if x_dist > 0:
                            move(tail, "R")
                        else:
                            move(tail, "L")

                        if y_dist > 0:
                            move(tail, "U")
                        else:
                            move(tail, "D")
                        
            visited.append(tuple(knots[-1]))

    return len(set(visited))


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
