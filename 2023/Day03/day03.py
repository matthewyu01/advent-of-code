
with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test1.txt','r') as f:
    test1 = [line[:-1] for line in f.readlines()]
try:
    with open('test2.txt','r') as f:
        test2 = [line[:-1] for line in f.readlines()]
except:
    test2 = test1
    

def symbol_near(r,c,grid):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False
    
    try:
        if not (grid[r+1][c].isnumeric() or grid[r+1][c] == '.'):
            return True
    except:
        pass
    try:
        if not (grid[r-1][c].isnumeric() or grid[r-1][c] == '.'):
            return True
    except:
        pass
    try:
        if not (grid[r][c+1].isnumeric() or grid[r][c+1] == '.'):
            return True
    except:
        pass
    try:
        if not (grid[r][c-1].isnumeric() or grid[r][c-1] == '.'):
            return True
    except:
        pass
    try:
        if not (grid[r+1][c+1].isnumeric() or grid[r+1][c+1] == '.'):
            return True
    except:
        pass
    try:
        if not (grid[r+1][c-1].isnumeric() or grid[r+1][c-1] == '.'):
            return True
    except:
        pass
    try:
        if not (grid[r-1][c+1].isnumeric() or grid[r-1][c+1] == '.'):
            return True
    except:
        pass
    try:
        if not (grid[r-1][c-1].isnumeric() or grid[r-1][c-1] == '.'):
            return True
    except:
        pass
    
    return False

from collections import defaultdict

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
            next = False
            if c == '.':
                pass
            if c.isnumeric():
                curr_num = c
                # print(curr_num)
                j = i + 1
                if not next:
                    next = symbol_near(r,i, grid)
                while j < len(l) and l[j].isnumeric():

                    curr_num += l[j]
                    if not next:
                        next = symbol_near(r,j, grid)
                    j += 1

                if next:
                    # print(curr_num)
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
            next = False
            curr_gear = None
            if c == '.':
                pass
            if c.isnumeric():
                # print(c)
                curr_num = c
                # print(curr_num)
                j = i + 1
                if not next:
                    next = gear_near(r,i, grid)
                    if next:
                        curr_gear = next
                while j < len(l) and l[j].isnumeric():

                    curr_num += l[j]
                    if not next:
                        next = gear_near(r,j, grid)
                        if next:
                            curr_gear = next
                    j += 1

                # print(curr_gear)
                if curr_gear:
                    # print(curr_num)
                    gears[curr_gear].append(curr_num)
                
                    
                i = j
                    
            elif c=='*': #symbol
                pass
            
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
