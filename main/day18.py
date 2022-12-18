from functools import reduce
from dataclasses import dataclass

@dataclass
class Cube:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash((self.x, self.y, self.z))

def get_neighbors(cube: Cube) -> list[Cube]:
    """Returns the neighbors for the given cube."""
    diffs = [Cube(-1, 0, 0), Cube(0, -1, 0), Cube(0, 0, -1), Cube(1, 0, 0), Cube(0, 1, 0), Cube(0, 0, 1)]
    neighbors = list(map(lambda diff: Cube(x=cube.x + diff.x, y=cube.y + diff.y, z=cube.z + diff.z), diffs))
    
    return neighbors

def common():
    with open('input/day18.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip().split(','), data))
        data = [Cube(int(x), int(y), int(z)) for x, y, z in data]

    return data

def part_one():
    cubes = common()

    # Slow approach but gets the job done... runtime of ~0.89s
    surface = 0
    for cube in cubes:
        surface += 6 - len(set(get_neighbors(cube)).intersection(cubes))

    return surface

def part_two():
    return

if __name__ == '__main__':
    print(part_one())
    print(part_two())
