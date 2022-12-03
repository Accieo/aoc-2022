from dataclasses import dataclass, field

@dataclass
class Elf:
    inventory: list = field(default_factory=list)
    calories: int = 0

def common():
    with open('input/day01.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))

    elf = Elf()
    elves = list()
    for n, item in enumerate(data):
        if item:
            elf.inventory.append(int(item))
            elf.calories += int(item)
            if n == len(data) - 1:
                elves.append(elf)
        else:
            elves.append(elf)
            elf = Elf()

    return elves

def part_one():
    elves = common()
    return max(elves, key=lambda x: x.calories).calories

def part_two():
    elves = common()
    elves.sort(key=lambda x: x.calories, reverse=True)
    return sum([elf.calories for elf in elves[0:3]])

if __name__ == '__main__':
    print(part_one())
    print(part_two())
