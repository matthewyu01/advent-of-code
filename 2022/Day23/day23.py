
with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test.txt','r') as f:
    test = [line[:-1] for line in f.readlines()]
    
from collections import defaultdict

def part1(lines=LINES): 
    TURNS = 10
    original_cols = len(lines[0])
    grid = [['.'] * (2*TURNS + original_cols) for _ in range(TURNS)] 
    # could've just used a set of elves without a grid lol
    elves = []

    dirs = [[(-1,-1),(-1,0),(-1,1)], #north
    [(1,-1),(1,0),(1,1)], #south
    [(-1,-1),(0,-1),(1,-1)], #west
    [(-1,1),(0,1),(1,1)]] #east to places to check, them move

    eight_dirs = [(r,c) for r in range(-1,2) for c in range(-1,2)]
    eight_dirs.remove((0,0))

    for line in lines:
        row = ['.'] * TURNS
        row.extend([c for c in line])
        row.extend(['.'] * TURNS)
        grid.append(row)
        
    for row in  [['.'] * (2*TURNS + original_cols) for _ in range(TURNS)]:
        grid.append(row)
    ROWS = len(grid)
    COLS = len(grid[0])
    for row in range(10, ROWS-10):
        for col in range(10, COLS - 10):
            c = grid[row][col]
            if c == '#':
                elves.append((row,col))

    round = 1
    while round <= TURNS:
        potential_new = defaultdict(int)
        new_spots = {}
        new_elves = []
        for i,elf in enumerate(elves):
            r,c = elf
            count = 0
            for dr,dc in eight_dirs:
                if grid[r+dr][c+dc] == '#':
                    count += 1
            
            if count == 0:
                new_elves.append(elf)
                continue
            for dir in dirs: # nesw
                c2 = 0
                for dr,dc in dir:
                    if grid[r+dr][c+dc] == '#':
                        c2 += 1
                        break
                if c2 > 0:
                    continue
                else:
                    step = dir[1]
                    new_r = r + step[0]
                    new_c = c + step[1]
                    new_spots[elf] = (new_r,new_c)
                    potential_new[(new_r,new_c)] += 1
                    break
            if elf not in new_spots:
                new_elves.append(elf)

        for elf in new_spots:
            if potential_new[new_spots[elf]] > 1:
                new_elves.append(elf)
                continue #can't move
            # can move
            r,c = elf
            grid[r][c] = '.'
            new_spot = new_spots[elf]
            r,c = new_spot
            grid[r][c] = '#'
            new_elves.append(new_spots[elf])

        elves = [elf for elf in new_elves]

            
        first = dirs.pop(0)
        dirs.append(first)
        round += 1     

    min_r = ROWS
    max_r = 0
    min_c = COLS
    max_c = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '#':
                min_r = min(r, min_r)
                max_r = max(r,max_r)
                min_c = min(min_c,c)
                max_c = max(c,max_c)
    
    ground = 0
    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c+1):
            if grid[r][c] == '.':
                ground += 1
    return ground


print(f'Part 1 Test Output: {part1(test)}' )
print(f'Part 1 ACTUAL: {part1(LINES)}' )

def part2(lines=LINES): 
    TURNS = 1000

    original_cols = len(lines[0])
    grid = [['.'] * (2*TURNS + original_cols) for _ in range(TURNS)]
    elves = []

    # 1 - north, 2- south, 3-  west, 4- east
    dirs = [[(-1,-1),(-1,0),(-1,1)], #north
    [(1,-1),(1,0),(1,1)], #south
    [(-1,-1),(0,-1),(1,-1)], #west
    [(-1,1),(0,1),(1,1)]] #east to places to check, them move

    eight_dirs = [(r,c) for r in range(-1,2) for c in range(-1,2)]
    eight_dirs.remove((0,0))

    for line in lines:
        row = ['.'] * TURNS
        row.extend([c for c in line])
        row.extend(['.'] * TURNS)
        grid.append(row)
        
    for row in  [['.'] * (2*TURNS + original_cols) for _ in range(TURNS)]:
        grid.append(row)
    ROWS = len(grid)
    COLS = len(grid[0])
    for row in range(10, ROWS-10):
        for col in range(10, COLS - 10):
            c = grid[row][col]
            if c == '#':
                elves.append((row,col))

    round = 1
    while round <= TURNS:
        potential_new = defaultdict(int)
        new_spots = {}
        new_elves = []
        for i,elf in enumerate(elves):
            r,c = elf
            count = 0
            for dr,dc in eight_dirs:
                if grid[r+dr][c+dc] == '#':
                    count += 1
            
            if count == 0:
                new_elves.append(elf)
                continue
            for dir in dirs: # nesw
                c2 = 0
                for dr,dc in dir:
                    if grid[r+dr][c+dc] == '#':
                        c2 += 1
                        break
                if c2 > 0:
                    continue
                else:
                    step = dir[1]
                    new_r = r + step[0]
                    new_c = c + step[1]
                    new_spots[elf] = (new_r,new_c)
                    potential_new[(new_r,new_c)] += 1
                    break
            if elf not in new_spots:
                new_elves.append(elf)

        for elf in new_spots:
            if potential_new[new_spots[elf]] > 1:
                new_elves.append(elf)
                continue #can't move
            # can move
            r,c = elf
            grid[r][c] = '.'
            new_spot = new_spots[elf]
            r,c = new_spot
            grid[r][c] = '#'
            new_elves.append(new_spots[elf])

        if set(elves) == set(new_elves):
            return round
        elves = [elf for elf in new_elves]


        first = dirs.pop(0) 
        dirs.append(first)
        round += 1

print(f'Part 2 Test Output: {part2(test)}' )
print(f'Part 2 ACTUAL: {part2(LINES)}' )
