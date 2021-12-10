""" https://adventofcode.com/2021/day/2 """

with open ('input.txt', 'r') as f:
    lines = f.readlines()

# Part 1
x = 0
depth = 0
for line in lines:
    c = line[0]
    num = int(line[line.find(' ')+1:-1])
    if c == 'f': #forward  
        x += num
    elif c =='d': #down
        depth += num   
    elif c =='u': #up
        depth -= num
print(f"Part 1: {depth*x}") #answer is product of depth and x position

# Part 2

def part2(lines):
    x = 0
    depth = 0
    aim = 0
    for line in lines:
        c = line[0]
        num = int(line[line.find(' ')+1:-1])
        if c == 'f': #forward  
            if aim > 0:
                depth += num * aim
            x += num
        elif c =='d': #down
            aim += num  
        elif c =='u': #up
            aim -= num
        # print(f"Depth: {depth}  X: {x} Aim: {aim}")
    print(f"Part 2: {depth*x}") #answer is product of depth and x position
    
test_lines = [
    'forward 5a',
    'down 5 ',
    'forward 8 ',
    'up 3 ',
    'down 8 ',
    'forward 2 ',
]
#part2(test_lines) == 900

part2(lines)