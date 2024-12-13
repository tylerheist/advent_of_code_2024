import re
from pathlib import Path

INPUT_LOCATION_PATH = Path('inputs/day_3.txt')
PATTERN = 'mul\([0-9]+,[0-9]+\)'
DISABLE = "don't()"
ENABLE = "do()"

def parse_input(fi: Path) -> str:
    with fi.open() as f:
        return f.read()
    
def find_and_apply_correct_multiply_instructions(instruction: str, pattern: str) -> int:
    correct_instructions = re.findall(pattern, instruction)
    products = []
    for inst in correct_instructions:
        numbers = re.findall('\d+', inst)
        products.append(int(numbers[0]) * int(numbers[1]))
    return sum(products)

def disable_multiply_instructions(instruction: str, pattern: str) -> int:
    disable_command_locs = [x.start() for x in re.finditer(DISABLE, instruction)]
    new_instruction = list(instruction)
    for loc in disable_command_locs:
        next_enable_loc = instruction.find(ENABLE, loc)
        if next_enable_loc < 0:
            next_enable_loc = len(instruction)
        new_instruction[loc:next_enable_loc] = "X" * (next_enable_loc - loc) 
    new_instruction = ''.join(new_instruction)
    print(new_instruction)
    return find_and_apply_correct_multiply_instructions(new_instruction, pattern)

if __name__ == "__main__":
    instruction = parse_input(INPUT_LOCATION_PATH)
    print(find_and_apply_correct_multiply_instructions(instruction, PATTERN))
    print(disable_multiply_instructions(instruction, PATTERN))
    
