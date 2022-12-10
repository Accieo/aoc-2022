from dataclasses import dataclass

@dataclass
class File:
    name: str
    size: int

    def __add__(self, other):
        return self.size + other.size

    def __radd__(self, other):
        return self.size.__add__(other)

def common():
    with open('input/day07.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip().split(' '), data))
        dirs = {}
        path = ['/']
        joined_path = ''

        for line in data:
            if '$' and 'cd' in line:
                _, _, dir = line
                if dir == '/':
                    path = ['/']
                elif dir == '..':
                    path.pop()
                else:
                    path.append(dir)

                joined_path = '/'.join(path)
                joined_path += '/'
                joined_path = joined_path[1:]
                if joined_path not in dirs.keys():
                    dirs[joined_path] = list()

            if line[0].isnumeric():
                size, name = line
                file = File(name, int(size))
                dirs[joined_path].append(file)

    for k in dirs.keys():
        dirs[k] = sum(dirs[k])

    for k in dirs.keys():
        for k2 in dirs.keys():
            if k2.startswith(k) and k2 != k:
                dirs[k] += dirs[k2]

    return dirs

def part_one():
    dirs = common()

    size_filtered = {k: v for k, v in dirs.items() if v <= 100_000}
    total = sum(size_filtered.values())

    return total

def part_two():
    dirs = common()

    disk_space = 70_000_000
    req_space = 30_000_000

    free_space = disk_space - dirs['/']
    size_filtered = {k: v for k, v in dirs.items() if free_space + v >= req_space}
    smallest_dir = min(size_filtered.values())

    return smallest_dir

if __name__ == '__main__':
    print(part_one())
    print(part_two())
