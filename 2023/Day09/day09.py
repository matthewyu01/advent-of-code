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


def next_num(nums):

    levels = {0:nums}

    lvl = 1

    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    while any(diffs):
        levels[lvl] = diffs

        diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
        lvl += 1
    levels[lvl] = diffs + [0]


    for i in range(lvl-1, -1, -1):
        curr = levels[i]
        curr.append(curr[-1] + levels[i+1][-1])
        levels[i] = curr

    return levels[0][-1]

def prev_num(nums):

    levels = {0:nums}

    lvl = 1

    diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    while any(diffs):
        levels[lvl] = diffs

        diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
        lvl += 1
    levels[lvl] =  [0] + diffs


    for i in range(lvl-1, -1, -1):
        curr = levels[i]
        curr.append(curr[0] - levels[i+1][-1])
        levels[i] = curr

    return levels[0][-1]

def part1(lines=LINES):
    res = 0
    i = 0

    map= dict()
    dirs = lines[0]

    while i < len(lines):
        line = lines[i]
        next_val = 0
        nums = [int(x) for x in line.split()]

        res += next_num(nums)

        i += 1




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

    while i < len(lines):
        line = lines[i]
        next_val = 0
        nums = [int(x) for x in line.split()]

        res += prev_num(nums)

        i += 1




    return res


print(f'Part 2 Test Output: {part1(test2)}' )
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {p2_actual}  COPIED!' )
