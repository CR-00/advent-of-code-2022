from utils import parse_input
import numpy as np

puzzle_input = [[int(x) for (x) in row] for row in parse_input(day="08")]

forest = np.array(puzzle_input)
x, y = forest.shape


def part_one():

    visible_trees = x * 2 - 2 + y * 2 - 2

    for i in range(1, x - 1):
        for j in range(1, y - 1):
        
            row = forest[i,:]
            col = forest[:,j]

            left = row[:j]
            right = row[j+1:]

            up = col[:i]
            down = col[i+1:]

            is_visible = False

            for direction in [up, left, right, down]:
                for tree in direction:
                    if tree >= forest[i,j]:
                        break
                else:
                    is_visible = True
        
            if is_visible:
                visible_trees += 1

    return visible_trees


def part_two():

    viewing_distances = []

    for i in range(1, x - 1):
        for j in range(1, y - 1):
        
            row = forest[i,:]
            col = forest[:,j]

            left = reversed(row[:j])
            right = row[j+1:]

            up = reversed(col[:i])
            down = col[i+1:]

            trees_visible = 1

            for direction in [up, left, right, down]:
                for k, tree in enumerate(direction):
                    if tree >= forest[i,j]:
                        break
        
                trees_visible *= k + 1
            
            viewing_distances += [trees_visible]

    return max(viewing_distances)





if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
