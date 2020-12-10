def get_instructions():
    instructions = []
    with open('input.txt','r') as f:
        for line in f.readlines():
            for part in line.split(','):
                if part.isdigit():
                    instructions.append(int(part))
    return instructions


def execute_instructions(instructions):
    length = len(instructions)
    i = 0
    while i < length:
        code = instructions[i]
        if code == 99:
            break
        elif code == 1 or code == 2:
            try:
                pos1 = instructions[i+1]
                pos2 = instructions[i+2]
                pos3 = instructions[i+3]
                if code == 1:
                    new_num = instructions[pos1] + instructions[pos2]
                elif code == 2:
                    new_num = instructions[pos1] * instructions[pos2]
                instructions[pos3] = new_num   

                i += 4 #step forward 4 positions
            except:
                print("Out of bounds error")
                return
        else:
            break

    return instructions[0]


def test_instructions(instructions,output):
    for noun in range(100):
        for verb in range(100): 
            codes = instructions.copy() #need copy bc pass by ref
            codes[1] = noun
            codes[2] = verb
            if execute_instructions(codes) == output:
                return noun,verb
    return -1, -1


if __name__ == "__main__":
    instructions = get_instructions()
    #part 1
    instructions[1] = 12
    instructions[2] = 2
    output = execute_instructions(instructions)
    print(output)
    #part 2
    instructions = get_instructions()
    n,v = test_instructions(instructions,19690720)
    print(100*n + v)
