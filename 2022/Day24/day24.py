
with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test.txt','r') as f:
    test = [line[:-1] for line in f.readlines()]
    
from collections import deque


def part1(lines=LINES): 
    right = set()
    left = set()
    up = set()
    down = set()
    dirs = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == '>':
                right.add((row,col))
            elif c == '<':
                left.add((row,col))
    
            elif c == '^':
                up.add((row,col))
    
            elif c == 'v':
                down.add((row,col))

    curr_r = 0
    curr_c = 1
    ROWS = len(lines)
    COLS = len(lines[0])
    # bfs per time
    mins = 0
    q = deque([(0,1)])

    while True:
        new_q = set()
        
        while q:

            curr_r, curr_c = q.popleft()
            new_q.add((curr_r,curr_c))
            for dr, dc in dirs.values():
                r2 = curr_r + dr
                c2 = curr_c + dc
                if 1<=r2<ROWS-1 and 1<=c2 < COLS - 1:
                    new_q.add((r2,c2))
                elif r2 == ROWS - 1 and c2 == COLS - 2: # exception to add end point as potential for next step
                    new_q.add((r2,c2))
            if curr_r == ROWS - 1 and curr_c == COLS - 2:
                return mins
        
        # move blizzards
        right = {(r,c+1) for r,c in right}
        for r,c in right:
            if c == COLS - 1:
                right.remove((r,c))
                right.add((r,1))

        left = {(r,c-1) for r,c in left}
        for r,c in left:
            if c == 0:
                left.remove((r,c))
                left.add((r,COLS - 2))

        down = {(r+1,c) for r,c in down}
        for r,c in down:
            if r == ROWS - 1:
                down.remove((r,c))
                down.add((1,c))

        up = {(r-1,c) for r,c in up}
        for r,c in up:
            if r == 0:
                up.remove((r,c))
                up.add((ROWS - 2, c))

        for b in left.intersection(new_q):
            new_q.remove(b)
        for b in right.intersection(new_q):
            new_q.remove(b)
        for b in up.intersection(new_q):
            new_q.remove(b)
        for b in down.intersection(new_q):
            new_q.remove(b)

        q = deque(list(new_q))
        #print(q)
        mins += 1

print(f'Part 1 Test Output: {part1(test)}' )
print(f'Part 1 ACTUAL: {part1(LINES)}' )


def part2(lines=LINES): 
    right = set()
    left = set()
    up = set()
    down = set()
    dirs = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == '>':
                right.add((row,col))
            elif c == '<':
                left.add((row,col))
    
            elif c == '^':
                up.add((row,col))
    
            elif c == 'v':
                down.add((row,col))

    mins = 0
    curr_r = 0
    curr_c = 1
    ROWS = len(lines)
    COLS = len(lines[0])

    # bfs per time
    mins = 0
    q = deque([(0,1)])

    first = True
    second = False
    third = False

    while True:
        new_q = set()
        while q:
            
            curr_r, curr_c = q.popleft()
            new_q.add((curr_r,curr_c))
            for dr, dc in dirs.values():
                r2 = curr_r + dr
                c2 = curr_c + dc
                if 1<=r2<ROWS-1 and 1<=c2 < COLS - 1:
                    new_q.add((r2,c2))
                elif r2 == ROWS - 1 and c2 == COLS - 2:
                    new_q.add((r2,c2))
                elif r2 == 0 and c2 == 1: # needed this exception to finish part 2, took me 15 minutes to figure this out...
                    new_q.add((r2,c2))
            if first and curr_r == ROWS - 1 and curr_c == COLS - 2:
                first = False
                second = True
                new_q = {(curr_r,curr_c), (ROWS-2, COLS-2)}
                #print(mins,'1')
                q = []
                break
                
            elif second and curr_r == 0 and curr_c == 1:
                third = True
                second = False
                #print(mins,'2')
                new_q = {(curr_r,curr_c), (1,1)}
                q = []
                break
                
            elif third and curr_r == ROWS - 1 and curr_c == COLS - 2:
                return mins
       
        # move blizzards
        right = {(r,c+1) for r,c in right}
        for r,c in right:
            if c == COLS - 1:
                right.remove((r,c))
                right.add((r,1))

        left = {(r,c-1) for r,c in left}
        for r,c in left:
            if c == 0:
                left.remove((r,c))
                left.add((r,COLS - 2))

        down = {(r+1,c) for r,c in down}
        for r,c in down:
            if r == ROWS - 1:
                down.remove((r,c))
                down.add((1,c))

        up = {(r-1,c) for r,c in up}
        for r,c in up:
            if r == 0:
                up.remove((r,c))
                up.add((ROWS - 2, c))
        
        
        for b in left.intersection(new_q):
            new_q.remove(b)
        for b in right.intersection(new_q):
            new_q.remove(b)
        for b in up.intersection(new_q):
            new_q.remove(b)
        for b in down.intersection(new_q):
            new_q.remove(b)

        q = deque(list(new_q))

        mins += 1
   
          
print(f'Part 2 Test Output: {part2(test)}' )
print(f'Part 2 ACTUAL: {part2(LINES)}' )
