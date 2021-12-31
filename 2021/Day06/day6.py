""" https://adventofcode.com/2021/day/6 """


def get_lines():
    with open('input.txt', 'r') as f:
        # ignore '\n' at end of each line
        return [line[:-1] for line in f.readlines()]


TEST_LINES = ['3,4,3,1,2']


def part1(DAYS, lines=get_lines()):
    line = [int(n) for n in lines[0].split(',')]
    for _ in range(DAYS):
        new_line = line.copy()
        for i in range(len(line)):
            new_line[i] -= 1
            if new_line[i] < 0:
                new_line[i] = 6  # reset to 6 days to produce more fish
                new_line.append(8)  # 8 days for first fish

        line = new_line.copy()

    print(len(line))
    return len(line)


def part2(DAYS, lines=get_lines()):
    line = [int(n) for n in lines[0].split(',')]

    # need to optimize

    # fish[i] = # of fish with timer i
    fish = [0]*9
    for n in line:
        fish[n] += 1

    for _ in range(DAYS):
        # shift array one to the left to simulate one day
        # fish[0] will be removed and added to the end (fish[8]) - new fish
        new = fish.pop(0)
        fish.append(new)
        fish[6] += new  # add fish[0] to fish[6] - timer reset

    return sum(fish)


if __name__ == '__main__':
    assert(part1(18, TEST_LINES) == 26)
    assert(part1(80, TEST_LINES) == 5934)
    print(f'Part 1: {part1(80)}')
    assert(part2(256, TEST_LINES) == 26984457539)
    print(f'Part 2: {part2(256)}')
