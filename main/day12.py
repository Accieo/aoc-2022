from heapq import heappop, heappush
from string import ascii_lowercase

heights = { k:v for k, v in zip(ascii_lowercase, range(len(ascii_lowercase))) }
heights['S'] = heights['a']
heights['E'] = heights['z']

def bfs_neighbors(i: int, j: int, max_y: int, max_x: int):
    up = (i - 1, j) if i != 0 else (i, j)
    down = (i + 1, j) if i != max_y else (i, j)
    left = (i, j - 1) if j != 0 else (i, j)
    right = (i, j + 1) if j != max_x else (i, j)

    return [up, down, left, right]

def breadth_first_search(graph: list[list[str]], root: tuple) -> int:
    heap = [(0, root)]
    explored = set([root])
    while heap:
        steps, (i, j) = heappop(heap)
        if graph[i][j] == 'E':
            return steps
        for neighbor in bfs_neighbors(i=i, j=j, max_y=len(graph) - 1, max_x=len(graph[0]) - 1):
            if heights[graph[neighbor[0]][neighbor[1]]] <= heights[graph[i][j]] + 1:
                if neighbor not in explored:
                    heappush(heap, (steps + 1, neighbor))
                    explored.add(neighbor)

    return 0

def common():
    with open('input/day12.txt', 'r') as file:
        data = file.read().splitlines()
        data = list(map(lambda x: list(x), data))

    return data

def part_one():
    graph = common()

    start_y, start_x = (0, 0)
    for i, line in enumerate(graph):
        if 'S' in line:
            start_y = i
            start_x = line.index('S')

    steps = breadth_first_search(graph=graph, root=(start_y, start_x))

    return steps

def part_two():
    graph = common()

    starts = list()
    for i, line in enumerate(graph):
        if 'a' in line:
            starts.append((i, line.index('a')))

    steps = min([breadth_first_search(graph=graph, root=start) for start in starts])

    return steps

if __name__ == '__main__':
    print(part_one())
    print(part_two())
