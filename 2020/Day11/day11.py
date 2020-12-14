

#floor (.), an empty seat (L), or an occupied seat (#)

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

def part1(grid):
    old_grid = grid[:]
    height = len(old_grid)
    width = len(old_grid[0])
    new_grid = old_grid[:]
    first = True

    while old_grid != new_grid or first:
        old_grid = new_grid[:]
        #print('New')
        # for row in old_grid:
        #     print(row)
        first = False
        for i,row in enumerate(old_grid):
            for j, char in enumerate(row):
                if char == 'L':
                    if i > 0:
                        if old_grid[i-1][j] == '#': #above
                            continue
                        if j > 0 and old_grid[i-1][j-1] == '#': #left above
                            continue
                        if j < width - 1 and old_grid[i-1][j+1] == '#': #right above
                            continue                        
                    if i < height - 1:
                        if old_grid[i+1][j] == '#': #below
                            continue     
                        if j > 0 and old_grid[i+1][j-1] == '#': #left below
                            continue
                        if j < width - 1 and old_grid[i+1][j+1] == '#': #right below
                            continue                               
                    if j > 0 and old_grid[i][j-1] == '#': #left
                        continue                                                   
                    if j < width - 1 and old_grid[i][j+1] == '#': #right
                        continue                                         
                    new_grid[i] = new_grid[i][:j] + '#' + new_grid[i][j+1:]

                elif char == '#':
                    occupied = 0
                    if i > 0:
                        if old_grid[i-1][j] == '#': #above
                            occupied += 1
                        if j > 0 and old_grid[i-1][j-1] == '#': #left above
                            occupied += 1
                        if j < width - 1 and old_grid[i-1][j+1] == '#': #right above
                            occupied += 1                        
                    if i < height - 1:
                        if old_grid[i+1][j] == '#': #below
                            occupied += 1     
                        if j > 0 and old_grid[i+1][j-1] == '#': #left below
                            occupied += 1
                        if j < width - 1 and old_grid[i+1][j+1] == '#': #right below
                            occupied += 1                               
                    if j > 0 and old_grid[i][j-1] == '#': #left
                        occupied += 1                                                 
                    if j < width - 1 and old_grid[i][j+1] == '#': #right
                        occupied += 1                              
                                   
                    if occupied >= 4:
                        new_grid[i] = new_grid[i][:j] + 'L' + new_grid[i][j+1:]                 
        
    occupied_seats = 0
    for row in new_grid:
        for char in row:
            if char =='#':
                occupied_seats += 1
    return occupied_seats


def part2(grid):
    # it now takes five or more visible occupied seats for an occupied seat to become empty 
    # The other rules still apply: empty seats that see no occupied seats become occupied, 
    # seats matching no rule don't change, and floor never changes.
    old_grid = grid[:]
    height = len(old_grid)
    width = len(old_grid[0])
    new_grid = old_grid[:]
    first = True

    while old_grid != new_grid or first:
        first = False
        for i,row in enumerate(old_grid):
            for j, char in enumerate(row):
                if char == 'L':        
                    pass

    return

def look_left_for_occupied(grid,i,j):
    row = i
    col = j
    
    while col > 0:
        char = grid[row][col-1] # left seat
        if char == '#': 
            return True
        elif char == '.': #floor
            pass
        else:
            return False
        col -= 1

    return False

def look_up_for_occupied(grid,i,j):
    row = i
    col = j
    
    while row > 0:
        char = grid[row-1][col] # above seat
        if char == '#': 
            return True
        elif char == '.': #floor
            pass
        else:
            return False
        row -= 1

    return False


def test_look_functions():
    assert(look_left_for_occupied(test_grid,3,0) == False)
    assert(look_left_for_occupied(test_grid,2,3) == True)
    assert(look_left_for_occupied(test_grid,3,3) == False)
    assert(look_up_for_occupied(test_grid,2,3) == False)
    assert(look_up_for_occupied(test_grid,2,2) == True)
    assert(look_up_for_occupied(test_grid,0,4) == False)
    assert(look_up_for_occupied(test_grid,5,5) == True)


if __name__ == "__main__":
    with open('input.txt','r') as f:
        grid = [line.strip() for line in f.readlines()]
    test_grid = [
        'L.LL.LL.LL',
        'LLLLLLL.LL',
        'L.L.L..L..', 
        'LLLL.LL.LL',
        'L.LL.LL.LL',
        'L.LLLLL.LL',
        '..L.L.....',
        'LLLLLLLLLL',
        'L.LLLLLL.L',
        'L.LLLLL.LL']
    #print(f"Part 1 Test: {part1(test_grid)}") #should be 37
    #print(f"Part 1: {part1(grid)}")
    test_grid = [
        '.##.##.',
        '#.#.#.#',
        '##...##',
        '...L...',
        '##...##',
        '#.#.#.#',
        '.##.##.',]
    test_look_functions()
    #print(f"Part 2: {part2(grid)}")


