def common():
    with open('input/day04.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip().split(','), data))

    return data

def part_one():
    data = common()
    fully_contained_count = 0
    for section in data:
        a, b = list(map(lambda x: x.split('-'), section))
        a = set(range(int(a[0]), int(a[1]) + 1))
        b = set(range(int(b[0]), int(b[1]) + 1))
        if a.intersection(b) == b or b.intersection(a) == a:
            fully_contained_count += 1
            
    return fully_contained_count

def part_two():
    data = common()
    fully_contained_count = 0
    for section in data: 
        a, b = list(map(lambda x: x.split('-'), section))
        a = set(range(int(a[0]), int(a[1]) + 1))
        b = set(range(int(b[0]), int(b[1]) + 1))
        if a.intersection(b) or b.intersection(a):
            fully_contained_count += 1
        
    return fully_contained_count

if __name__ == '__main__':
    print(part_one())
    print(part_two())
