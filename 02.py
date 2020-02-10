SEPARATOR = ","
FILENAME = "files/02.txt"

def get_operand(num):
    if num == 1:
        return "+"
    elif num == 2:
        return "*"
    elif num == 99:
        return False
    else:
        raise ValueError("Invalid operand")

def get_program(filename):
    with open(filename) as f:
        program = f.readline().rstrip().split(SEPARATOR)
        return program
index = 0
program = get_program(FILENAME)
while True:
    operand = get_operand(int(program[index]))
    if operand:
        operator1 = program[int(program[index+1])]
        operator2 = program[int(program[index+2])]
        value = eval(f"{operator1}{operand}{operator2}")
        program[int(program[index+3])] = value
        index += 4
    else:
        break
print(program)
