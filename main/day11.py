from math import prod, lcm
from dataclasses import dataclass, field

@dataclass
class Monkey:
    inventory: list[int] = field(default_factory=list)
    operation: str = ''
    divisor: int = 0
    true_throw: int = 0
    false_throw: int = 0
    amount_inspected: int = 0

def run_rounds(monkeys: list[Monkey], rounds: int, worried: bool = False) -> list[Monkey]:
    
    least_common_multiple = lcm(*[monkey.divisor for monkey in monkeys])

    for _ in range(rounds):
        to_pop = [0 for _ in range(len(monkeys))]
        for n, monkey in enumerate(monkeys):
            for x in monkey.inventory:                # x is used inside eval
                worry_level = eval(monkey.operation)

                if not worried:
                    worry_level //= 3
                else:
                    worry_level %= least_common_multiple

                if worry_level % monkey.divisor == 0:
                    monkeys[monkey.true_throw].inventory.append(worry_level)
                else:
                    monkeys[monkey.false_throw].inventory.append(worry_level)

                to_pop[n] += 1
                monkey.amount_inspected += 1

        for amount, monkey in zip(to_pop, monkeys):
            monkey.inventory = monkey.inventory[amount:]

    return monkeys

def common():
    with open('input/day11.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))
        data.append('')

        monkeys = list()
        monkey = Monkey()
        for line in data:
            if 'items' in line:
                starting_items = line.split(':')[1].split(',')
                starting_items = list(map(lambda x: int(x.strip()), starting_items))
                monkey.inventory = starting_items
            elif 'Operation' in line:
                operation = line.split('=')[1].strip().replace('old', 'x')
                operation = f'{operation}'   
                monkey.operation = operation
            elif 'Test' in line:
                divisor = int(line.split(' ')[-1])
                monkey.divisor = divisor
            elif 'true' in line:
                true_throw = int(line.split(' ')[-1])
                monkey.true_throw = true_throw
            elif 'false' in line:
                false_throw = int(line.split(' ')[-1])
                monkey.false_throw = false_throw
            elif line == '':
                monkeys.append(monkey)
                monkey = Monkey()

    return monkeys

def part_one():
    monkeys = common()

    monkeys = run_rounds(monkeys=monkeys, rounds=20, worried=False)
    inspected_items = [monkey.amount_inspected for monkey in monkeys]
    inspected_items.sort()

    monkey_business = prod(inspected_items[-2:])

    return monkey_business

def part_two():
    monkeys = common()
    
    monkeys = run_rounds(monkeys=monkeys, rounds=10_000, worried=True)
    inspected_items = [monkey.amount_inspected for monkey in monkeys]
    inspected_items.sort()

    monkey_business = prod(inspected_items[-2:])

    return monkey_business

if __name__ == '__main__':
    print(part_one())
    print(part_two())
