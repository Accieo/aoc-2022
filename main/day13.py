from functools import cmp_to_key
from itertools import chain
from typing import Union

def compare_lists(left: list[Union[int, list]], right: list[Union[int, list]]) -> int:

    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1          # Keep alive

    if isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            outcome = compare_lists(left=left[i], right=right[i])
            if outcome == 1:
                return 1
            elif outcome == -1:
                return -1

            i += 1

        if i == len(left):
            if len(left) == len(right):
                return 0    # Go next
            return 1        # Left side finished first
        elif i == len(right):
            return -1       # Keep alive

    return 0 # Redundant

def common(divider_packets: bool = False):
    with open('input/day13.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))
        data.append('')

        pairs = list()
        tmp = list()
        for line in data:
            if line != '':
                tmp.append(line)
            elif len(tmp) == 2:
                pairs.append(tmp)
                tmp = list()

        if divider_packets:
            pairs.append(['[[2]]', '[[6]]'])

    return pairs

def part_one():
    pairs = common()

    total = 0
    for idx, (left, right) in enumerate(pairs, start=1):
        if compare_lists(eval(left), eval(right)) == 1:
            total += idx

    return total

def part_two():
    pairs = common(divider_packets=True)
    pairs = list(chain.from_iterable(pairs))
    pairs = list(map(eval, pairs))
    pairs = sorted(pairs, key=cmp_to_key(compare_lists), reverse=True)
    pkg2 = pairs.index([[2]]) + 1
    pkg6 = pairs.index([[6]]) + 1
    decoder_key = pkg2 * pkg6

    return decoder_key

if __name__ == '__main__':
    print(part_one())
    print(part_two())
