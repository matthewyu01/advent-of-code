""" https://adventofcode.com/2021/day/5 """
from collections import defaultdict


def get_lines():
    with open('input.txt', 'r') as f:
        # ignore '\n' at end of each line
        return [line[:-1] for line in f.readlines()]


TEST_LINES = ['0,9 -> 5,9',
              '8,0 -> 0,8',
              '9,4 -> 3,4',
              '2,2 -> 2,1',
              '7,0 -> 7,4',
              '6,4 -> 2,0',
              '0,9 -> 2,9',
              '3,4 -> 1,4',
              '0,0 -> 8,8',
              '5,5 -> 8,2', ]


def part1(lines=get_lines()):
    points = defaultdict(int)

    for line in lines:
        arr = line.split(' ')
        coord1 = arr[0]
        coord2 = arr[2]
        x1 = int(coord1.split(',')[0])
        y1 = int(coord1.split(',')[1])
        x2 = int(coord2.split(',')[0])
        y2 = int(coord2.split(',')[1])

        if x1 == x2:
            if y2 < y1:  # swap so range is going up
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                points[(x1, y)] += 1
        elif y1 == y2:
            if x2 < x1:  # swap so range is going up
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                points[(x, y1)] += 1

    count = 0
    for point in points:
        if points[point] > 1:
            count += 1

    print(f'# of Points with Overlap: {count}')
    return count


def part2(lines=get_lines()):
    points = defaultdict(int)

    for line in lines:
        arr = line.split(' ')
        coord1 = arr[0]
        coord2 = arr[2]
        x1 = int(coord1.split(',')[0])
        y1 = int(coord1.split(',')[1])
        x2 = int(coord2.split(',')[0])
        y2 = int(coord2.split(',')[1])

        if x1 == x2:
            if y2 < y1:  # swap so range is going up
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                points[(x1, y)] += 1
        elif y1 == y2:
            if x2 < x1:  # swap so range is going up
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                points[(x, y1)] += 1
        # case for diagonal lines
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx == dy:  # diagonal or just one point
            step_x = 1
            step_y = 1
            if x2 < x1:
                step_x = -1
            if y2 < y1:
                step_y = -1
            for i in range(dx+1):
                points[(x1+i*step_x, y1+i*step_y)] += 1

    count = 0
    for point in points:
        if points[point] > 1:
            count += 1

    print(f'# of Points with Overlap: {count}')
    return count


if __name__ == '__main__':
    assert(part1(TEST_LINES) == 5)
    part1()
    assert(part2(TEST_LINES) == 12)
    part2()