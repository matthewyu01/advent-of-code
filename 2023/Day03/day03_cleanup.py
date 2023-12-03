with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test1.txt','r') as f:
    test1 = [line[:-1] for line in f.readlines()]
try:
    with open('test2.txt','r') as f:
        test2 = [line[:-1] for line in f.readlines()]
except:
    test2 = test1
    
from collections import defaultdict
    

def symbol_near(r,c,grid):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    
    diffs = [(1,0),(-1,0),
    (1,1),(-1,1),
    (1,-1),(-1,-1),
    (0,1),(0,-1),]
    
    for d in diffs:
        dr = r + d[0]
        dc = c + d[1]
        try:
            if not (grid[dr][dc].isnumeric() or grid[dr][dc] == '.'):
                return True
        except:
            pass
        
  
    return False


def gear_near(r,c,grid):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    
    diffs = [(1,0),(-1,0),
    (1,1),(-1,1),
    (1,-1),(-1,-1),
    (0,1),(0,-1),]
    
    for d in diffs:
        dr = r + d[0]
        dc = c + d[1]
        try:
            if grid[dr][dc] == '*':
                return (dr,dc)
        except:
            pass
        
  
    return False


def part1(lines=LINES): 
    grid = [[c for c in line] for line in lines]
    res = 0
    for r,l in enumerate(lines):
        i = 0
        while i < len(l):
            c = l[i]
            curr_num = ''
            next_to_gear = False
            if c == '.':
                pass
            elif c.isnumeric():
                curr_num = c
                j = i + 1
                if not next_to_gear:
                    next_to_gear = symbol_near(r,i, grid)
                while j < len(l) and l[j].isnumeric():
                    curr_num += l[j]
                    if not next_to_gear:
                        next_to_gear = symbol_near(r,j, grid)
                    j += 1

                if next_to_gear:
                    res += int(curr_num)
                  
                i = j
                    
            else: #symbol
                pass
            
            i += 1
        
    return res


print(f'Part 1 Test Output: {part1(test1)}' )
print(f'Part 1 ACTUAL: {part1(LINES)}' )


def part2(lines=LINES):     
    grid = [[c for c in line] for line in lines]
    res = 0
    gears = defaultdict(list)

    for r,l in enumerate(lines):
        i = 0
        while i < len(l):
            c = l[i]
            curr_num = ''
            next_to_gear = False
            curr_gear = None
            if c == '.':
                pass
            if c.isnumeric():
                curr_num = c
                j = i + 1
                
                if not next_to_gear:
                    next_to_gear = gear_near(r,i, grid)
                    if next_to_gear:
                        curr_gear = next_to_gear
                while j < len(l) and l[j].isnumeric():

                    curr_num += l[j]
                    if not next_to_gear:
                        next_to_gear = gear_near(r,j, grid)
                        if next_to_gear:
                            curr_gear = next_to_gear
                    j += 1

                if curr_gear:
                    gears[curr_gear].append(curr_num)
                
                    
                i = j
            
            i += 1
            
    res = 0
    for k in gears:
        l = gears[k]
        if len(l) == 2:
            print(k, l)
            res += int(l[0]) * int(l[1])
        
    return res
          
          
print(f'Part 2 Test Output: {part2(test2)}' )
print(f'Part 2 ACTUAL: {part2(LINES)}' )
