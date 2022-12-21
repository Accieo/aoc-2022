import re

def eval_instruction(instructions: dict, parent: str):
    if isinstance(instructions[parent], int):
        return instructions[parent]
    else:
        children = re.findall("'.*?'", instructions[parent])
        children = list(map(lambda x: x.replace("'", ''), children))
        operation = re.findall('[+-/*]', instructions[parent])
        left = eval_instruction(instructions=instructions, parent=children[0]) 
        right = eval_instruction(instructions=instructions, parent=children[1]) 
        return eval(f'{left} {operation[0]} {right}')
        
def common():
    with open('input/day21.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))

        instructions = dict()
        for instruction in data:
            split_inst = instruction.split(':')
            key = split_inst[0].strip()
            split_op = split_inst[1].split(' ')
            if len(split_op) > 2:
                instructions[key] = ' '.join([f"instructions['{split_op[1]}']", split_op[2], f"instructions['{split_op[3]}']"])
            else:
                instructions[key] = int(split_inst[1].strip())

    return instructions

def part_one():
    instructions = common()

    answer = int(eval_instruction(instructions=instructions, parent='root'))
    
    return answer

def part_two():
    return

if __name__ == '__main__':
    print(part_one())
    print(part_two())
