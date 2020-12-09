def run_instructions_1(code):
    lines_read = {}
    accumulator = 0
    line_num = 0
    while line_num < len(code):
        line = code[line_num]
        if lines_read.get(line_num):
            return accumulator

        lines_read[line_num] = 1 #add to dict

        instruction = line[:3]

        if instruction == "nop":
            line_num += 1
            continue

        num = int(line[5:-1]) #new line char at end
        if line[4] == '-': 
            num *= -1
        if instruction == "jmp":
            line_num += num
            continue
        elif instruction == "acc":
            accumulator += num
        line_num += 1




def run_instructions_2(code,max_change_count):
    changed_count = 0
    while changed_count < max_change_count:
        lines_read = {}
        accumulator = 0
        line_num = 0
        infinite_loop = False
        nop_jmp_encountered = 0

        while line_num < len(code):
            line = code[line_num]
            if lines_read.get(line_num):
                infinite_loop = True
                break

            lines_read[line_num] = 1 #add to dict

            instruction = line[:3]

            if nop_jmp_encountered == changed_count: #change nth instruction
                if instruction == "nop":
                    instruction = "jmp"
                elif instruction == "jmp":
                    instruction = "nop"

            if instruction == "nop":
                nop_jmp_encountered += 1
                line_num += 1
                continue

            num = int(line[5:-1]) #new line char at end
            if line[4] == '-': 
                num *= -1

            if instruction == "jmp":
                nop_jmp_encountered += 1
                line_num += num
                continue

            elif instruction == "acc":
                accumulator += num
            line_num += 1

        changed_count += 1

        if not infinite_loop:
            return accumulator

     
if __name__ == "__main__":
    with open('input.txt','r') as f:
        lines = f.readlines()

    change_count = 0
    for line in lines:
        if line[:3] == "nop" or line[:3] == "jmp":
            change_count += 1 

    print(run_instructions_1(lines))
    print(run_instructions_2(lines,change_count))