from dataclasses import dataclass

@dataclass
class Particle:
    x: int = 0
    y: int = 0

@dataclass
class Move:
    dir: str
    mag: int

def chebyshev(p1: Particle, p2: Particle):
    return max(abs(p2.x - p1.x), abs(p2.y - p1.y))

def chebyshev_move(head: Particle, tail: Particle):
    if chebyshev(head, tail) == 2:
        if head.y > tail.y and head.x > tail.x:      # UR
            tail.y += 1
            tail.x += 1
        elif head.y < tail.y and head.x > tail.x:    # DR
            tail.y -= 1
            tail.x += 1
        elif head.y > tail.y and head.x < tail.x:    # UL
            tail.y += 1
            tail.x -= 1
        elif head.y < tail.y and head.x < tail.x:    # DL
            tail.y -= 1
            tail.x -= 1
        elif head.y > tail.y and head.x == tail.x:   # CU
            tail.y += 1
        elif head.y < tail.y and head.x == tail.x:   # CD
            tail.y -= 1
        elif head.y == tail.y and head.x > tail.x:   # CR
            tail.x += 1
        elif head.y == tail.y and head.x < tail.x:   # CL
            tail.x -= 1

def step_by_step(move: Move, heads: list[Particle]):
    visited = list()
    for _ in range(0, move.mag):
        match move.dir:
            case 'R':
                heads[0].x += 1
            case 'L':
                heads[0].x -= 1
            case 'U':
                heads[0].y += 1
            case 'D':
                heads[0].y -= 1
        for n in range(0, len(heads) - 1):
            chebyshev_move(heads[n], heads[n+1])

        visited.append((heads[-1].x, heads[-1].y))

    return visited

def common(particles: int):
    with open('input/day09.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip().split(' '), data))
        moves = [Move(d, int(m)) for d, m in data]

        heads = [Particle() for _ in range(particles)]

        visited = list()
        for move in moves:
            visited.append(step_by_step(move, heads))

        visited = [i for j in visited for i in j]
        unique_visited = len(set(visited))

    return unique_visited

def part_one():
    return common(particles=2)

def part_two():
    return common(particles=10)

if __name__ == '__main__':
    print(part_one())
    print(part_two())
