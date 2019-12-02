import sys

def parse_opcode(memory, pc):
    return (memory[pc], memory[pc+1], memory[pc+2], memory[pc+3])


def execute_instruction(memory, pc):
    if memory[pc] == 99:
        return False
    opcode, input_one, input_two, output = parse_opcode(memory, pc) 
    if opcode == 1:
        memory[output] = memory[input_one] + memory[input_two]
        return True
    elif opcode == 2:
        memory[output] = memory[input_one] * memory[input_two]
        return True


def run_program(memory, pc):
    while execute_instruction(memory, pc):
        pc += 4


with open('input.txt') as f:
    program = [int(value) for value in f.read().split(',')]

# Part 1
memory = program.copy()
memory[1] = 12
memory[2] = 2
run_program(memory, 0)
print(f"Answer to part 1: {memory[0]}")

# Part 2
for x in range(100):
    for y in range(100):
        memory = program.copy()
        memory[1] = x
        memory[2] = y

        run_program(memory, 0)

        if memory[0] == 19690720:
            result = 100 * memory[1] + memory[2]
            print(f"Answer to part 2: {result}")
            sys.exit()
        


