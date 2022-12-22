from copy import deepcopy

def mix(sequence: list[tuple[int, int]], amount: int = 1) -> list[tuple[int, int]]:
    original = deepcopy(sequence)

    for _ in range(amount):
        for idx, num in original:
            old_pos = sequence.index((idx, num))
            popped = sequence.pop(old_pos)
            new_pos = (old_pos + num) % (len(original) - 1)
            sequence.insert(new_pos, popped)

    return sequence

def mix_lookup(mixed: list[tuple[int, int]], index: int) -> int:
    zero_element = list(filter(lambda x: x[1] == 0, mixed))[0]
    zero_index = mixed.index(zero_element)
    target = mixed[(zero_index + index) % len(mixed)][1]

    return target
    
def common():
    with open('input/day20.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: (x[0], int(x[1].strip())), enumerate(data, start=0)))

    return data

def part_one():
    encrypted = common()

    mixed = mix(sequence=encrypted)

    x = mix_lookup(mixed=mixed, index=1000)
    y = mix_lookup(mixed=mixed, index=2000)
    z = mix_lookup(mixed=mixed, index=3000)
    
    total = sum([x, y, z])
    
    return total

def part_two():
    encrypted = common()

    decrypted = list(map(lambda x: (x[0], x[1] * 811589153), encrypted))

    # Mixing is a bit slow... runtime of ~1.59s
    mixed = mix(sequence=decrypted, amount=10)

    x = mix_lookup(mixed=mixed, index=1000)
    y = mix_lookup(mixed=mixed, index=2000)
    z = mix_lookup(mixed=mixed, index=3000)
    
    total = sum([x, y, z])

    return total

if __name__ == '__main__':
    print(part_one())
    print(part_two())
