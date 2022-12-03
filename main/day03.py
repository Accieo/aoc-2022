from string import ascii_lowercase, ascii_uppercase
from dataclasses import dataclass

@dataclass
class Rucksack:
    cmp_one: str = ''
    cmp_two: str = ''

prio_lowercase = { letter:prio for letter, prio in zip(ascii_lowercase, range(1,27)) }
prio_uppercase = { letter:prio for letter, prio in zip(ascii_uppercase, range(27,53)) }
prio_list = { **prio_lowercase, **prio_uppercase }

with open('examples/day03.txt', 'r') as file:
    data = file.read().splitlines()

def common():
    rucksack = Rucksack()
    rucksacks = list()
    for items in data:
        items_amount = len(items)
        rucksack.cmp_one = items[:items_amount//2]
        rucksack.cmp_two = items[items_amount//2:]
        rucksacks.append(rucksack)
        rucksack = Rucksack()

    return rucksacks

def part_one():
    rucksacks = common()
    priority_sum = 0
    for rucksack in rucksacks:
        cmp_one = set(rucksack.cmp_one)
        cmp_two = set(rucksack.cmp_two)
        intersection = cmp_one.intersection(cmp_two)
        priority_sum += prio_list[list(intersection)[0]]

    return priority_sum

def part_two():
    return

if __name__ == '__main__':
    print(part_one())
    print(part_two())
