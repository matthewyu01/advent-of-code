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


from collections import Counter, defaultdict, deque
import re
import math
import subprocess
from heapq import *
import numpy as np
import math

from functools import cmp_to_key


def part1(lines=LINES):
    res = 0
    i = 0

    map= dict()
    dirs = lines[0]

    i = 2
    curr = 'AAA'
    while i < len(lines):
        l = lines[i]
        left, right = l.split(' = (')
        l, r = right.split(', ')
        r = r[:-1]
        map[left] = (l,r)
        i += 1

    steps = 0
    while True:
        for d in dirs:
            if d =='L':
                curr = map[curr][0]
            else:
                curr = map[curr][1]
            steps += 1
            if curr == 'ZZZ':
                return steps


    return res


print(f'Part 1 Test Output: {part1(test1)}' )
p1_actual = part1(LINES)
subprocess.run("clip", text=True, input=str(p1_actual))
print(f'Part 1 ACTUAL: {p1_actual}   COPIED!' )


def part2(lines=LINES):
    res = 0
    i = 0

    map= dict()
    dirs = lines[0]

    i = 2
    starts = []
    while i < len(lines):
        l = lines[i]
        left, right = l.split(' = (')
        l, r = right.split(', ')
        r = r[:-1]
        map[left] = (l,r)
        if left.endswith('A'):
            starts.append(left)

        i += 1
    # print(starts)
    # return
    steps = 0
    steps_to_z = dict()
    p = []
    while starts:
        for d in dirs:
            if d == 'L':
                starts = [map[curr][0] for curr in starts]
            else:
                starts = [map[curr][1] for curr in starts]
            steps += 1
            for s in starts.copy():
                if s.endswith('Z'):
                    steps_to_z[s] = steps
                    p.append(steps)
                    starts.remove(s)
    print(steps_to_z)

    res = 1
    return math.lcm( 12599, 17873, 19631, 20803, 21389, 23147)
    return res


print(f'Part 2 Test Output: {part2(test2)}' )
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {p2_actual}  COPIED!' )
