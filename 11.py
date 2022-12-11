import math
import operator
from utils import parse_input

puzzle_input = parse_input(day="11")


ops = {
    '+' : operator.add,
    '*' : operator.mul,
}


class Monkey:

    def __init__(
        self,
        number,
        items,
        test,
        op,
        operand,
        if_true,
        if_false
    ):
        self.number = number
        self.items = items
        self.test = test

        self.op = op
        self.operand = operand

        self.if_true = if_true
        self.if_false = if_false

        self.peers = []

        self.inspect_count = 0
        self.target = None

    def inspect(self):

        if self.operand == "old":
            ev = ops[self.op](self.items[0], self.items[0])
        else:
            ev = ops[self.op](self.items[0], int(self.operand))

        self.items[0] = self.base(ev)
        self.inspect_count += 1
    
    def throw(self):
   
        if self.items[0] % self.test == 0:
            self.target = self.if_true
        else:
            self.target = self.if_false
 
        for peer in self.peers:
            if peer.number in self.target:
                peer.items.append(self.items.pop(0))
        

def driver(part):

    monkeys = []

    m = {}

    for row in puzzle_input:

        if "Monkey" in row:     
            m["number"] = row.split(" ")[1].replace(":", "")

        elif "Starting items:" in row:
            m["items"] = list(map(int, row.replace(",", "").split(" ")[4:]))

        elif "Operation" in row:
            _, _, _, op, operand = row.split(" ")[3:]
            m["op"] = op
            m["operand"] = operand

        elif "Test" in row:
            m["test"] = int(row.split(" ")[-1])

        elif "If true" in row:
           m["if_true"] = " ".join(row.split()[2:])

        elif "If false" in row:
            m["if_false"] = " ".join(row.split()[2:])

            monkeys.append(Monkey(**m))

    if part == 1:
        base = lambda x: x // 3
    else:
        lcm = math.lcm(*(m.test for m in monkeys))
        base = lambda x: x % lcm
    
    for m in monkeys:
        m.peers = monkeys
        m.base = base

    return monkeys


def part_one():
    monkeys = driver(part=1)
    for _ in range(20):
        for m in monkeys:
            while m.items:
                m.inspect()
                m.throw()

    inspects = [m.inspect_count for m in monkeys]
    return math.prod(sorted(inspects, reverse=True)[:2])


def part_two():
    monkeys = driver(part=2)
    for _ in range(10000):
        for m in monkeys:
            while m.items:
                m.inspect()
                m.throw()

    inspects = [m.inspect_count for m in monkeys]
    return math.prod(sorted(inspects, reverse=True)[:2])


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    

