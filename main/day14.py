from math import sqrt

def drop_sand(cave: list[list[str]], until_source: bool = False) -> int:
    """Returns amount of sand dropped before it begins falling into the abyss."""

    blockers = ['o', '#']
    source_index = cave[0].index('+')
    abyss_not_found = True
    dropped_sand = 0

    while abyss_not_found:
        height = 0
        pos = source_index
        while height < len(cave) - 1:
            if not until_source:
                if pos >= len(cave[0]) - 1:
                    abyss_not_found = False
                    break
            else:
                if cave[0][source_index] == 'o':
                    abyss_not_found = False
                    break

            if cave[height + 1][pos] not in blockers:
                height += 1
                continue

            if cave[height + 1][pos - 1] not in blockers:
                height += 1
                pos -= 1
                continue
            
            if cave[height + 1][pos + 1] not in blockers:
                height += 1
                pos += 1
                continue

            cave[height][pos] = 'o'
            dropped_sand += 1
            break
        else:
            abyss_not_found = False

    return dropped_sand

def common(floor: bool = False):
    with open('input/day14.txt', 'r') as file:
        data = file.read().splitlines()
        data = list(map(lambda x: x.replace(' ','').split('->'), data))
        data = list(map(lambda x: list((int(y.split(',')[0]), int(y.split(',')[1])) for y in x), data))
        
        x_coords = [x for path in data for x, _ in path]
        min_x = min(x_coords)
        max_x = max(x_coords)
        max_y = max([y for path in data for _, y in path])

        cave = [['.' for _ in range((max_x + 1) - min_x)] for _ in range(max_y + 1)]
        for path in data:
            for j, (x, y) in enumerate(path):
                prev_x = path[j - 1][0] if j != 0 else j
                prev_y = path[j - 1][1] if j != 0 else j
                cave[y][x - min_x] = '#'
                if prev_x == x:
                    if prev_y > y:
                        for i in range(prev_y, y, -1):
                            cave[i][x - min_x] = '#'
                    else:
                        for i in range(prev_y, y):
                            cave[i][x - min_x] = '#'
                if prev_y == y:
                    if prev_x > x:
                        for i in range(prev_x, x, -1):
                            cave[y][i - min_x] = '#'
                    else:
                        for i in range(prev_x, x):
                            cave[y][i - min_x] = '#'

        # Set starting point
        cave[0][500 - min_x] = '+'

        if floor:
            pythagoras = int(sqrt(len(cave)**2 + (len(cave[0])//2)**2))
            for i in range(len(cave)):
                for _ in range(pythagoras):
                    cave[i].insert(0, '.')
                    cave[i].append('.')

            cave.append(['.' for _ in range(len(cave[0]))])
            cave.append(['.' for _ in range(len(cave[0]))])
            for i in range(len(cave[0])):
                cave[-1][i] = '#'

    return cave

def part_one():
    cave = common()

    dropped_sand = drop_sand(cave=cave)

    return dropped_sand

def part_two():
    cave = common(floor=True)

    dropped_sand = drop_sand(cave=cave, until_source=True)

    return dropped_sand

if __name__ == '__main__':
    print(part_one())
    print(part_two())
