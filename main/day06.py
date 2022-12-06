def common(char_size: int):
    with open('input/day06.txt', 'r') as file:
        data = file.readlines()
        signal = data[0].strip()

    lo_range = range(0, len(signal), 1)
    hi_range = range(char_size, len(signal) + char_size, 1)
    markers = set()
    for i, j in zip(lo_range, hi_range):
        markers.update(list(signal[i:j]))
        if len(markers) == char_size:
            return i + char_size
        else:
            markers = set()

def part_one():
    return common(char_size=4)
    
def part_two():
    return common(char_size=14)

if __name__ == '__main__':
    print(part_one())
    print(part_two())
