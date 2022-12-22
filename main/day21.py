import re

def eval_instruction(instructions: dict, parent: str):
    if isinstance(instructions[parent], int):
        return instructions[parent]
    else:
        children = re.findall("'.*?'", instructions[parent])
        children = list(map(lambda x: x.replace("'", ''), children))
        operation = ''.join(re.findall('[+-/*=]', instructions[parent]))
        left = int(eval_instruction(instructions=instructions, parent=children[0]))
        right = int(eval_instruction(instructions=instructions, parent=children[1]))
        #if parent == 'root': Check if brute forced num is getting close
        #   print(left, right)
        return eval(f'{left} {operation} {right}')

def set_human(instructions: dict, human: int):
    instructions['humn'] = human
    return instructions
        
def common(root_match: bool = False):
    with open('input/day21.txt', 'r') as file:
        data = file.readlines()
        data = list(map(lambda x: x.strip(), data))

        instructions = dict()
        for instruction in data:
            split_inst = instruction.split(':')
            key = split_inst[0].strip()
            split_op = split_inst[1].split(' ')
            if len(split_op) > 2:
                left = f"instructions['{split_op[1]}']"
                right = f"instructions['{split_op[3]}']"
                instructions[key] = ' '.join([left, split_op[2], right])
            else:
                instructions[key] = int(split_inst[1].strip())

        if root_match:
            instructions['root'] = instructions['root'].replace('+', '==')
            return instructions

    return instructions

def part_one():
    instructions = common()

    answer = int(eval_instruction(instructions=instructions, parent='root'))
    
    return answer

def part_two():
    instructions = common(root_match=True)
    
    not_found = False
    human = 3_352_886_133_830 # Brute force gang
    while not not_found:
        human += 1
        instructions = set_human(instructions=instructions, human=human)
        not_found = eval_instruction(instructions=instructions, parent='root')

    return human

if __name__ == '__main__':
    print(part_one())
    print(part_two())
