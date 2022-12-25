def snafu_to_dec(snafu_number: str) -> int:
    """Converts a SNAFU number to decimal"""
    numerical_system = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }
    numbers = list(map(lambda num: numerical_system[num], snafu_number))
    multipliers = [5 ** n for n in reversed(range(len(snafu_number)))]

    result = sum(list(map(lambda x: x[0] * x[1], zip(numbers, multipliers))))
    
    return result

def dec_to_snafu(dec_number: int) -> str:
    """Converts a decimal number to SNAFU. Refer to Balanced Ternary Number Systems."""
    snafu_num = ''
    while dec_number != 0:
        mod = dec_number % 5
        dec_number //= 5

        if mod <= 2:
            snafu_num += str(mod)
        else:
            snafu_num += '=' if mod == 3 else '-'
            dec_number += 1

    snafu_num = snafu_num[::-1]

    return snafu_num

def common():
    with open('input/day25.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))

    return data

def part_one():
    data = common()

    result = sum([snafu_to_dec(snafu_number=num) for num in data])
    result = dec_to_snafu(result)

    return result

def part_two():
    return 'Merry Christmas'

if __name__ == '__main__':
    print(part_one())
    print(part_two())
