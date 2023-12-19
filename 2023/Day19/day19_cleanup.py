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


import re
import subprocess


def part1(lines=LINES):
    res = 0
    i = 0

    workflows = dict()
    parts = []
    while i < len(lines):
        line = lines[i]
        i += 1
        if line == '':
            break
        workflow, right = line.split('{')
        right = right[:-1]

        conditions = right.split(',')
        workflows[workflow] = conditions


    while i < len(lines):
        line = lines[i][1:-1]
        nums = [int(x) for x in re.findall("\d+", line)] # doesnt do negatives
        parts.append(nums)
        i += 1


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

    workflows = dict()
    while i < len(lines):
        line = lines[i]
        i += 1
        if line == '':
            break
        workflow, right = line.split('{')
        right = right[:-1]

        conditions = right.split(',')
        workflows[workflow] = conditions


    from copy import deepcopy

    # [[(1,4000), (1,4000), (1,4000), (1,4000)],'in']
    # split intervals based on conditions (like in a decision tree)
    def next(intervals):
        new_intervals = []
        skip = False
        for i in intervals:
            x, m, a, s, curr = i
            if curr == 'A':
                new_intervals.append(i)
                continue

            conditions = workflows[curr]
            last = conditions[-1]

            current_interval = [x,m,a,s,curr]

            for c in conditions[:-1]:
                condition, res = c.split(':')
                letter = condition[0]
                if letter == 'x':
                    j = 0
                if letter == 'm':
                    j = 1
                if letter == 'a':
                    j = 2
                if letter == 's':
                    j = 3
                if '<' in condition:
                    condition_num = int(condition.split('<')[-1])

                    min_, max_ = current_interval[j]
                    # < condition_num
                    if min_ < condition_num <= max_:
                        met_condition = [min_, condition_num-1]
                        current_interval[j] = deepcopy(met_condition)
                        current_interval[-1] = res
                        new_intervals.append(deepcopy(current_interval))
                        current_interval[j] = [condition_num, max_]
                    elif condition_num > max_:
                        current_interval[-1] = res
                        skip = True
                        new_intervals.append(deepcopy(current_interval))
                        break
                elif '>' in condition:
                    condition_num = int(condition.split('>')[-1])

                    min_, max_ = current_interval[j]
                    # > condition_num
                    if min_ <= condition_num < max_:
                        met_condition = [condition_num+1, max_] # didn't swap these two and took so long to find bug
                        current_interval[j] = deepcopy(met_condition)
                        current_interval[-1] = res
                        new_intervals.append(deepcopy(current_interval))
                        current_interval[j] = [min_, condition_num] # didn't swap these two and took so long to find bug
                    elif condition_num < min_:
                        current_interval[-1] = res
                        skip = True
                        new_intervals.append(deepcopy(current_interval))
                        break

            if not skip:
                current_interval[-1] = last
                new_intervals.append(current_interval)
            else:
                break

        return new_intervals

    # each "interval" contains 5 elemetnts: min and max for `x,m,a,s` plus the current node
    prev_intervals = [[[1,4000], [1,4000], [1,4000], [1,4000], 'in']]

    for i in range(100): # 100 iterations was enough to reach all accept states, but i should check to see if previous and next intervals are equal and break
        next_intervals = deepcopy(next(prev_intervals))
        next_intervals = [x for x in next_intervals if x[-1] !='R']

        prev_intervals = deepcopy(next_intervals)

    next_intervals = [x for x in next_intervals if x[-1] == 'A']

    for x in next_intervals:
        p = 1
        # [1, 1415], [1, 4000], [1, 2005], [1, 1350], 'A']
        for nums in x[:-1]:
            p *= (int(nums[1]) - int(nums[0]) + 1)
        res += p

    return res


print(f'Part 2 Test Output: {part2(test2)}' )
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {p2_actual}  COPIED!' )
