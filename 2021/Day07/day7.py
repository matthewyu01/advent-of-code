""" https://adventofcode.com/2021/day/7 """


def get_line():
    with open('input.txt', 'r') as f:
        # ignore '\n' at end of each line
        return [int(n) for n in f.readlines()[0].split(',')]

TEST_LINE = [16,1,2,0,4,2,7,1,2,14]


def part1(line = get_line()):
    mi = ma = line[0]
    
    for n in line: #find max and minimum
        ma = max(ma, n)
        mi = min(mi, n)
    
    approx = round((sum(line) - ma - mi) / len(line)) - 1 # approximate value for best position

    def fuel_cost(pos):
        diff = 0
        for n in line:
            diff += abs(n - pos)
        return diff

    best_fuel = fuel_cost(approx)

    #increase
    for i in range(approx+1, len(line)):
        if fuel_cost(i) < best_fuel:
            best_fuel = fuel_cost(i)
            best_pos = i
        else:
            break
    #decrease
    for i in range(approx-1, -1,-1):
        if fuel_cost(i) < best_fuel:
            best_fuel = fuel_cost(i)
            best_pos = i
        else:
            break
    return best_fuel


def part2(line = get_line()):
    mi = ma = line[0]
    
    for n in line: #find max and minimum
        ma = max(ma, n)
        mi = min(mi, n)
    
    approx = round((sum(line)) / len(line)) - 1 # approximate value for best position

    def fuel_cost(pos):
        diff = 0
        for n in line:
            delta = abs(n - pos)
            diff += delta * (delta+1) // 2
        return diff

    best_fuel = fuel_cost(approx)

    #increase
    for i in range(approx+1, len(line)):
        if fuel_cost(i) < best_fuel:
            best_fuel = fuel_cost(i)
            best_pos = i
        else:
            break
    #decrease
    for i in range(approx-1, -1,-1):
        if fuel_cost(i) < best_fuel:
            best_fuel = fuel_cost(i)
            best_pos = i
        else:
            break
    return best_fuel

if __name__ == '__main__':
    assert(part1(TEST_LINE) == 37)
    
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')