import sys


def execute_instruction(memory, pc):
    if memory[pc] == 99:
        return False
    opcode, input_one, input_two, output = memory[pc:pc+4]
    if opcode == 1:
        memory[output] = memory[input_one] + memory[input_two]
        return True
    elif opcode == 2:
        memory[output] = memory[input_one] * memory[input_two]
        return True


def run_program(memory, pc=0):
    while execute_instruction(memory, pc):
        pc += 4


with open('input.txt') as f:
    program = [int(value) for value in f.read().split(',')]

# Part 1
memory = program.copy()
memory[1], memory[2] = 12, 2
run_program(memory)
print(f"Answer to part 1: {memory[0]}")

# Part 2
for x in range(100):
    for y in range(100):
        memory = program.copy()
        memory[1], memory[2] = x, y

        run_program(memory)

        if memory[0] == 19690720:
            result = 100 * x + y
            print(f"Answer to part 2: {result}")
            sys.exit()
