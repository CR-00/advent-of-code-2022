def parse_input(day):
    data = []
    with open(f"./inputs/{day}.txt", "r") as f:
        for line in f.readlines():
            data += [line.strip("\n")]
    return data