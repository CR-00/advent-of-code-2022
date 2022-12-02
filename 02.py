from utils import parse_input


puzzle_input = [i.split() for i in parse_input(day="02")]


def part_one():

    total_score = 0

    for opponents_move, my_move in puzzle_input:

        opponents_shape = ord(opponents_move) % 65 % 3
        my_shape = ord(my_move) % 65 % 23
        
        # Always add score of shape for round regardless of result.
        total_score += my_shape + 1

        # We win.
        if (opponents_shape + 1) % 3 == my_shape: 
            total_score += 6

        # It's a draw.
        elif opponents_shape == my_shape:
            total_score += 3

        # Opponent wins.
        else:
            ...

    return total_score


def part_two():

    total_score = 0

    for opponents_move, my_move in puzzle_input:

        # Must add 1 afterwards to fix the padding.
        opponents_shape = ord(opponents_move) % 65
    
        # We need to lose.
        if my_move == "X":
            total_score += (opponents_shape + 2) % 3 + 1
        
        # We need to draw.
        elif my_move == "Y":
            total_score += opponents_shape + 1
            total_score += 3

        # We need to win.
        else:
            total_score += (opponents_shape + 1) % 3 + 1
            total_score += 6

    return total_score


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")