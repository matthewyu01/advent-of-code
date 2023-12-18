with open('input.txt','r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test1.txt','r') as f:
    test1 = [line[:-1] for line in f.readlines()]
try:
    with open('test2.txt','r') as f:
        test2 = [line[:-1] for line in f.readlines()]
    if len(test2) == 0:
        test2 = [l for l in test1]
except:
    test2 = [l for l in test1]

#f.read().split("\n\n")

from collections import Counter, defaultdict, deque
import re
import math
import subprocess
from heapq import *
import numpy as np
import math

from itertools import *
from functools import cmp_to_key
# hand2 = sorted(h1.keys(),  key=cmp_to_key(sort_higher_card))
# np.prod
# math.lcm(*lst)
from matplotlib import path
def part1(lines=LINES):

    res = 0
    i = 0


    # ROWS = len(lines)
    # COLS = len(lines[0])

    # grid = np.array([[c for c in line] for line in lines])

    # ROWS, COLS = grid.shape
    # nums = np.array([[int(x) for x in line.split()] for line in lines])

    d = dict()
    dirs = {
        'U':(-1,0),
        'D':(1,0),
        'R':(0,1),
        'L':(0,-1)
    }

    # from shapely.geometry import Point
    # from shapely.geometry.polygon import Polygon
    r, c = 0,0

    pts = set([(0, 0)])
    mar = 0
    mir = 0
    mic = 0
    mac = 0
    lefts = {0:0}
    rights = {0:0}
    while i < len(lines):
        line = lines[i]

        dir, num, color = line.split(' ')
        num = int(num)

        hex = color[2:-1]
        num = int(hex[:-1], 16)
        encode = {'0':'R', '1':'D', "2":'L','3':'U'}
        dir = encode[hex[-1]]

        dr,dc = dirs[dir]
        if r in lefts:
            lefts[r] = min(lefts[r], c)
        else:
            lefts[r] = c
        if r in rights:
            rights[r] = max(rights[r], c)
        else:
            rights[r] = c
        pts.add((r,c))
        for _ in range(num):
            r += dr
            c += dc
            # p = Point(r,c)
            if r in lefts:
                lefts[r] = min(lefts[r], c)
            else:
                lefts[r] = c
            if r in rights:
                rights[r] = max(rights[r], c)
            else:
                rights[r] = c

            mar = max(mar,r)
            mir = min(mir,r)

            mac = max(mac,c)
            mic = min(mic,c)

            pts.add((r,c))

        next_val = 0
        # nums2 = re.findall("\d+", line) # doesnt do negatives
        # nums = [int(x) for x in line.split()]



        i += 1


    # just bfs from inside...  spent an hour on matplotlib polygon, shapely polygon, and poitn in polygon.
    # modified point-in-polygon should work to handle edge case


    # print(len(pts), 'len')
    # polygon = path.Path(list(pts))
    # print(polygon.area)
    new = set()

    q = deque([(1,1)])


    while q:
        curr = q.popleft()
        new.add((curr))
        r,c = curr
        for dr,dc in dirs.values():
            next = (r+dr, c+dc)
            if next not in pts and next not in new:
                new.add(next)
                q.append(next)
    return len(new | pts)

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def part2(lines=LINES):

    res = 0
    i = 0

    pts = [(0,0)]

    dirs = {
        'U':(-1,0),
        'D':(1,0),
        'R':(0,1),
        'L':(0,-1)
    }

    r, c = 0,0


    mar = 0
    mir = 0
    mic = 0
    mac = 0
    lefts = {0:0}
    rights = {0:0}
    while i < len(lines):
        line = lines[i]


        dir, num, color = line.split(' ')
        num = int(num)

        hex = color[2:-1]
        num = int(hex[:-1], 16)
        encode = {'0':'R', '1':'D', "2":'L','3':'U'}
        dir = encode[hex[-1]]

        dr,dc = dirs[dir]
        if r in lefts:
            lefts[r] = min(lefts[r], c)
        else:
            lefts[r] = c
        if r in rights:
            rights[r] = max(rights[r], c)
        else:
            rights[r] = c

        r += dr * num
        c += dc * num
        # p = Point(r,c)
        if r in lefts:
            lefts[r] = min(lefts[r], c)
        else:
            lefts[r] = c
        if r in rights:
            rights[r] = max(rights[r], c)
        else:
            rights[r] = c

        mar = max(mar,r)
        mir = min(mir,r)

        mac = max(mac,c)
        mic = min(mic,c)

        pts.append((r,c))

        i += 1


    polygon = Polygon(pts)
    # print(polygon)


    return polygon.area + sum(abs(p[0] - p2[0]) + abs(p[1] - p2[1]) for p, p2 in pairwise(pts))//2 + 1 # i just guessed the dividing by 2 this after undershooting, then overshooting test answer
    # https://en.wikipedia.org/wiki/Pick's_theorem is why it works


print(f'Part 2 Test Output: {part2(test2)}' )
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {p2_actual}  COPIED!' )
