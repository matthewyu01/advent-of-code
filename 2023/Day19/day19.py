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
# np.prod6
# math.lcm(*lst)

def part1(lines=LINES):

    res = 0
    i = 0


    # ROWS = len(lines)
    # COLS = len(lines[0])

    # grid = np.array([[c for c in line] for line in lines])

    # ROWS, COLS = grid.shape
    # nums = np.array([[int(x) for x in line.split()] for line in lines])

    workflows = dict()
    parts = []
    while i < len(lines):
        line = lines[i]
        if line == '':
            i += 1
            break
        # splt = line.split()
        workflow, right = line.split('{')
        right = right[:-1]



        conditions = right.split(',')
        workflows[workflow] = conditions

        next_val = 0
        # nums2 = re.findall("\d+", line) # doesnt do negatives
        # nums = [int(x) for x in line.split()]



        res += 0
        i += 1



    while i < len(lines):
        line = lines[i]
        line = line[1:-1]
        nums = []
        nums = [int(x) for x in re.findall("\d+", line)] # doesnt do negatives
        parts.append(nums)
        i += 1
    print(parts)

    # for cond in conditions:
    #     left,right = cond.split(':')



    #     print(conditions)

    def next(p, curr):
        flow = curr
        x, m, a, s = p
        x = int(x)
        m = int(m)
        a = int(a)
        s = int(s)
        conditions = workflows[curr]
        for c in conditions[:-1]:
            condition, res = c.split(':')
            # print(condition, res, p)
            if eval(condition):
                flow = res
                break
        else:
            flow = conditions[-1]

        return flow

    for p in parts:
        x, m, a, s = p
        curr = 'in'

        while curr != 'A' and  curr != 'R':

            curr = next(p,curr)

        if curr == 'A':
            res += int(x) + int(m) + int(a) + int(s)





    return res


print(f'Part 1 Test Output: {part1(test1)}' )
p1_actual = part1(LINES)
subprocess.run("clip", text=True, input=str(p1_actual))
print(f'Part 1 ACTUAL: {p1_actual}   COPIED!' )



def part2(lines=LINES):

    res = 0
    i = 0


    # ROWS = len(lines)
    # COLS = len(lines[0])

    # grid = np.array([[c for c in line] for line in lines])

    # ROWS, COLS = grid.shape
    # nums = np.array([[int(x) for x in line.split()] for line in lines])

    workflows = dict()
    parts = []
    while i < len(lines):
        line = lines[i]
        if line == '':
            i += 1
            break
        # splt = line.split()
        workflow, right = line.split('{')
        right = right[:-1]



        conditions = right.split(',')
        workflows[workflow] = conditions

        next_val = 0




        res += 0
        i += 1


    # interval reverse engineer
    from copy import deepcopy

    # [[(1,4000), (1,4000), (1,4000), (1,4000)],]
    def next(intervals):
        new = []
        skip = False
        for i in intervals:
            x, m, a, s, curr = i
            if curr == 'A':
                new.append(i)
                continue


            conditions = workflows[curr]
            last = conditions[-1]

            old_curr = deepcopy([x,m,a,s,curr])


            for c in conditions[:-1]:
                condition, res = c.split(':')
                # print(condition, res, p)
                letter = condition[0]
                if '<' in condition:
                    condition_num = int(condition.split('<')[-1])
                    if letter == 'x':
                        j = 0
                    if letter == 'm':
                        j = 1
                    if letter == 'a':
                        j = 2
                    if letter == 's':
                        j = 3
                    mn, max_ = old_curr[j]
                    # < condition_num
                    if mn < condition_num <= max_:
                        print('met')
                        met_condition = deepcopy([mn, condition_num-1])
                        old_curr[j] = deepcopy(met_condition)
                        old_curr[-1] = res
                        new.append(deepcopy(old_curr))
                        old_curr[j] = deepcopy([condition_num, max_])
                    elif condition_num > max_:
                        old_curr[-1] = res
                        skip = True
                        new.append(deepcopy(old_curr))
                        break
                elif '>' in condition:
                    condition_num = int(condition.split('>')[-1])
                    if letter == 'x':
                        j = 0
                    if letter == 'm':
                        j = 1
                    if letter == 'a':
                        j = 2
                    if letter == 's':
                        j = 3
                    mn, max_ = old_curr[j]
                    #= > condition_num
                    if mn <= condition_num < max_:
                        print('met')

                        met_condition = deepcopy([condition_num+1, max_])# didn't swap these two and took so long to find bug
                        old_curr[j] = deepcopy(met_condition)
                        old_curr[-1] = res
                        new.append(deepcopy(old_curr))
                        old_curr[j] = deepcopy([mn, condition_num])# didn't swap these two and took so long to find bug
                    elif condition_num < mn:
                        old_curr[-1] = res
                        skip = True
                        new.append(deepcopy(old_curr))
                        break


            # old_curr[-1] = last
            # new.append(deepcopy(old_curr))
            if not skip:
                old_curr[-1] = last

                new.append(deepcopy(old_curr))
            else:
                print('skipped')
                break



        return new

    start = [[[1,4000], [1,4000], [1,4000], [1,4000], 'in']]
    # two = next(start)
    # while True:
    #     if two == start:
    #         break
    for i in range(100):

        two = deepcopy(next(start))
        print(start, '\nnew',two, '')
        two = [x for x in two if x[-1] !='R']

        start = deepcopy(two)




    two = [x for x in two if x[-1] == 'A']
    res = 0
    # print(two)
    # return``
    for row in two:
        print(row)
    # return
    two.sort()
    for x in two:
        p = 1
        # [1, 1415], [1, 4000], [1, 2005], [1, 1350], 'A']
        for nums in x[:-1]:
            # print(nums)
            p *= (int(nums[1]) - int(nums[0]) + 1)

        res += p
        print(res, 'test')
    return res
    two = [x[:-1] for x in two]
    # print(two)


    two.sort()

    for r in two:
        print(r)





    return res


print(f'Part 2 Test Output: {part2(test2)}' )
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {p2_actual}  COPIED!' )
