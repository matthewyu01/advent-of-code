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


from collections import Counter,  defaultdict, deque
import re
import math
import subprocess
from heapq import *
import numpy as np


def part1(lines=LINES):
    res = 0

    for r, line in enumerate(lines):
        line = line.split(': ')[1]
        winning, cards = line.split(' | ')

        # print(winning, '\n',
        #       cards)

        nums = re.findall("\d+", winning)
        num2 = re.findall("\d+", cards)
        # print(nums)
        cnt = 0
        for n in num2:
            if n in nums:
                # print(n)
                cnt += 1
        # print(cnt)
        if cnt:
            res += 2**(cnt-1)


    return res


print(f'Part 1 Test Output: {part1(test1)}' )
p1_actual = part1(LINES)
subprocess.run("clip", text=True, input=str(p1_actual))
print(f'Part 1 ACTUAL: {part1(LINES)}   COPIED!' )


def part2(lines=LINES):
    res = 0
    cards = len(lines)
    # print(cards, 'cards')

    count = {c:1 for c in range(cards)}

    for r, line in enumerate(lines):
        line = line.split(': ')[1]
        winning, cards = line.split(' | ')

        # print(winning, '\n',
        #       cards)

        nums = re.findall("\d+", winning)
        num2 = re.findall("\d+", cards)
        # print(nums)
        cnt = 0
        for n in num2:
            if n in nums:
                # print(n)
                cnt += 1
        # print(cnt)

        for next in range(cnt):
            count[r + next + 1] += count[r]

        if cnt:
            res += 2**(cnt-1)
    return sum(count.values())


print(f'Part 2 Test Output: {part2(test2)}' )
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {part2(LINES)}  COPIED!' )
