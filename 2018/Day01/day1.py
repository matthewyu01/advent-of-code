with open('input.txt','r') as f:
    lines = f.readlines()

def part1():
    num = 0

    for line in lines:
        if line[0] == '+':
            num += int(line[1:].strip())
        else:
            num -= int(line[1:].strip())

    return num


def part2():
    numbers_been = {0:1}
    num = 0
    while True:
        for line in lines:
            if line[0] == '+':
                num += int(line[1:].strip())
            else:
                num -= int(line[1:].strip())
            if numbers_been.get(num) != None: #already in dict
                return num
            numbers_been[num] = 1
    

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")