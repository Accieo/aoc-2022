from dataclasses import dataclass

@dataclass
class Instruction:
    cmd: str
    val: int = 0

def print_crt(crt: list[list[str]]):
    for strip in crt:
        print(''.join(strip))

def common():
    with open('input/day10.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip().split(' '), data))
        instructions = list()
        for inst in data:
            if len(inst) < 2:
                instructions.append(Instruction(inst[0]))
            else:
                instructions.append(Instruction(inst[0], int(inst[1])))

    register = [1]
    for inst in instructions:
        if inst.cmd == 'noop':
            register.append(register[-1])
        else:
            register.append(register[-1])
            register.append(register[-1] + inst.val)

    return register

def part_one():
    register = common()

    to_add = [(val, register[val-1]) for val in range(20, 240, 40)]
    total = sum(list(map(lambda x: x[0] * x[1], to_add)))

    return total

def part_two():
    # Thanks 0xmycf for explaining the problem statement
    register = common()

    sections = list()
    for i, j in zip(range(0, len(register) - 40, 40), range(40, len(register), 40)):
        sections.append(register[i:j])

    crt = [['.' for _ in range(40)] for _ in range(6)]

    for s, section in enumerate(sections):
        for i, num in enumerate(section):
            if num == i - 1 or num == i or num == i + 1:
                crt[s][i] = '#'

    print_crt(crt)

if __name__ == '__main__':
    print(part_one())
    part_two()
