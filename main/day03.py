from string import ascii_lowercase, ascii_uppercase
from dataclasses import dataclass

@dataclass
class Rucksack:
    items: str = ''

prio_lowercase = { letter:prio for letter, prio in zip(ascii_lowercase, range(1,27)) }
prio_uppercase = { letter:prio for letter, prio in zip(ascii_uppercase, range(27,53)) }
prio_list = { **prio_lowercase, **prio_uppercase }

with open('input/day03.txt', 'r') as file:
    data = file.read().splitlines()

def common():
    rucksack = Rucksack()
    rucksacks = list()
    for items in data:
        rucksack.items = items
        rucksacks.append(rucksack)
        rucksack = Rucksack()

    return rucksacks

def part_one():
    rucksacks = common()
    priority_sum = 0
    for rucksack in rucksacks:
        items_amount = len(rucksack.items)
        cmp_one = set(rucksack.items[:items_amount//2])
        cmp_two = set(rucksack.items[items_amount//2:])
        intersection = cmp_one.intersection(cmp_two)
        priority_sum += prio_list[list(intersection)[0]]

    return priority_sum

def part_two():
    rucksacks = common()
    priority_sum = 0
    for i, j in zip(range(0, len(rucksacks) + 1, 3), range(3, len(rucksacks) + 1, 3)):
        elf_one, elf_two, elf_three = rucksacks[i:j]
        intersection = set(elf_one.items).intersection(elf_two.items, elf_three.items)
        priority_sum += prio_list[list(intersection)[0]]

    return priority_sum

if __name__ == '__main__':
    print(part_one())
    print(part_two())
