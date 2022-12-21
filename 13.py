import json
from utils import parse_input


puzzle_input = parse_input(day="13")


def in_order(p1, p2):

    if type(p1) is int and type(p2) is int:
        return p1 - p2
    
    if type(p1) is list and type(p2) is list:

        for _p1, _p2 in zip(p1, p2):
            are_in_order = in_order(_p1, _p2)
            if are_in_order:
                return are_in_order

        return len(p1) - len(p2)

    if type(p1) is int:
        return in_order([p1], p2)
    
    if type(p2) is int:
        return in_order(p1, [p2])



def part_one():

    ans = 0

    for i in range(0, len(puzzle_input), 3):
        
        idx = i // 3 + 1

        p1 = json.loads(puzzle_input[i])
        p2 = json.loads(puzzle_input[i + 1])

        if in_order(p1, p2) < 0:
            ans += idx

    return ans


def part_two():

    pckts = [[[2]], [[6]]]

    for i in range(0, len(puzzle_input), 3):
        pckts.append(json.loads(puzzle_input[i]))
        pckts.append(json.loads(puzzle_input[i + 1]))

    for i in range(len(pckts)):
        for j in range(0, len(pckts) - i - 1):            
            if in_order(pckts[j], pckts[j+1]) < 0:
                pckts[j], pckts[j+1] = pckts[j+1], pckts[j]
                
    ans = 1
    for i, p in enumerate(reversed(pckts)):
        if p == [[6]] or p == [[2]]:
            ans *= (i + 1)
    
    return ans


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    