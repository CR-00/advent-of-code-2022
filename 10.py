from utils import parse_input
import numpy as np

puzzle_input = parse_input(day="10")

def part_one():

    register = 1
    cycles = 0

    signal_intervals = [20, 60, 100, 140, 180, 220]

    signal_strengths = {}

    for instruction in puzzle_input:

        cycles += 1

        if cycles in signal_intervals:
            signal_strengths[cycles] = register
        
        if "addx" in instruction:

            operand = int(instruction.split()[1])

            cycles += 1

            if cycles in signal_intervals:
                signal_strengths[cycles] = register

            register += operand

    ans = 0
    for k, v in signal_strengths.items():
        ans += k * v

    return ans
  

def part_two():

    # Set up the screen.
    screen = np.chararray([6, 41])
    screen[:] = str(".")
    screen = np.array(screen, dtype=str)

    # Pretty print the answer.
    np.set_printoptions(linewidth=np.inf)

    register = 1
    cycles = 0

    for instruction in puzzle_input:
        
        x = register
        y = cycles // 40
        sprite = [(y, x-1), (y, x), (y, x+1)]

        # Draw the current cycle
        pixel = (cycles // 40, cycles % 40)

        # Noop always takes 1 cycle.
        cycles += 1

        # Check whether this causes overlap.
        if pixel in sprite:
            screen[pixel] = "#"

        if "addx" in instruction:

            operand = int(instruction.split()[1])

            # addx takes another cycle.
            pixel = (cycles // 40, cycles % 40)

            # Move the sprite, register may have changed.
            x = register
            y = cycles // 40
            sprite = [(y, x-1), (y, x), (y, x+1)]

            # Overlap
            if pixel in sprite:
                screen[pixel] = "#"

            cycles += 1
            
            register += operand

    return screen


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two:")
    print(part_two())


        