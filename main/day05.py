from dataclasses import dataclass

@dataclass
class Moves:
    amount: int = 0
    src: int = 0
    dst: int = 0

def common():
    with open('input/day05.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.replace('\n', ''), data))
        lo_range = range(0, len(data[0]) + 4, 4)
        hi_range = range(4, len(data[0]) + 4, 4)
        stacks = dict()
        for line in data:
            if '1' in line:
                for num in line.strip().split('   '):
                    stacks[int(num)] = list()
                break

        for line in data:
            if '[' in line:
                for n, (i, j) in enumerate(zip(lo_range, hi_range)):
                    crate = line[i:j].strip()
                    if crate:
                        stacks[n + 1].append(crate)
            else:
                break

        moves = list()
        for line in data:
            if 'move' in line:
                _, amount, _, src, _, dst = line.split(' ')
                moves.append(Moves(int(amount), int(src), int(dst)))
               
    return stacks, moves

def part_one():
    stacks, moves = common()
    for move in moves:
        for _ in range(0, move.amount):
            grabbed_crate = stacks[move.src].pop(0)
            stacks[move.dst].insert(0, grabbed_crate)

    top_crates = ''.join([v[0] for _, v in stacks.items()]).replace('[','').replace(']','')

    return top_crates

def part_two():
    stacks, moves = common()
    grabbed_crates = list()
    for move in moves:
        for _ in range(0, move.amount):
            grabbed_crates.append(stacks[move.src].pop(0))
        stacks[move.dst] = grabbed_crates + stacks[move.dst]
        grabbed_crates = list()

    top_crates = ''.join([v[0] for _, v in stacks.items()]).replace('[','').replace(']','')

    return top_crates

if __name__ == '__main__':
    print(part_one())
    print(part_two())
