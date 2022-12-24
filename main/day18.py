from typing import Union
from dataclasses import dataclass

@dataclass
class Cube:
    x: Union[int, float]
    y: Union[int, float]
    z: Union[int, float]

    def __hash__(self):
        return hash((self.x, self.y, self.z))

def get_neighbors(cube: Cube) -> list[Cube]:
    """Returns the neighbors for the given cube."""
    diffs = [Cube(-1, 0, 0), Cube(0, -1, 0), Cube(0, 0, -1), Cube(1, 0, 0), Cube(0, 1, 0), Cube(0, 0, 1)]
    neighbors = list(map(lambda diff: Cube(x=cube.x + diff.x, y=cube.y + diff.y, z=cube.z + diff.z), diffs))
    
    return neighbors

def get_faces(cube: Cube) -> list[Cube]:
    """Returns the faces for the given cube."""
    diffs = [Cube(-0.5, 0, 0), Cube(0, -0.5, 0), Cube(0, 0, -0.5), Cube(0.5, 0, 0), Cube(0, 0.5, 0), Cube(0, 0, 0.5)]
    faces = list(map(lambda diff: Cube(x=cube.x + diff.x, y=cube.y + diff.y, z=cube.z + diff.z), diffs))

    return faces

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
    cubes = common()
    
    # Also a slow approach, taking ~5s
    min_x = min_y = min_z = 0
    max_x = max_y = max_z = 0

    # Surround the lava droplet
    for cube in cubes:
        min_x = min(min_x, cube.x)
        min_y = min(min_y, cube.y)
        min_z = min(min_z, cube.z)
        max_x = max(max_x, cube.x)
        max_y = max(max_y, cube.y)
        max_z = max(max_z, cube.z)

    min_x, min_y, min_z = list(map(lambda x: x - 1, [min_x, min_y, min_z]))
    max_x, max_y, max_z = list(map(lambda x: x + 1, [max_x, max_y, max_z]))

    queue = [Cube(min_x, min_y, min_z)]
    exterior = {Cube(min_x, min_y, min_z)}

    while queue:
        cube = queue.pop(0)
        for neighbor in get_neighbors(cube):
            if not (min_x <= neighbor.x <= max_x and min_y <= neighbor.y <= max_y and min_z <= neighbor.z <= max_z):
                continue
            if neighbor in exterior or neighbor in cubes:
                continue

            queue.append(neighbor)
            exterior.add(neighbor)

    exterior_faces = set()
    for cube in exterior:
        exterior_faces.update(get_faces(cube))

    droplet_faces = set()
    for cube in cubes:
        droplet_faces.update(get_faces(cube))

    total = len(exterior_faces.intersection(droplet_faces))

    return total

if __name__ == '__main__':
    print(part_one())
    print(part_two())
