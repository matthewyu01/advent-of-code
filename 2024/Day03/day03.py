with open('input.txt', 'r') as f:
    LINES = [line[:-1] for line in f.readlines()]
with open('test1.txt', 'r') as f:
    test1 = [line[:-1] for line in f.readlines()]
# with open('test2.txt', 'r') as f:
#     test2 = [line[:-1] for line in f.readlines()]

import re
from collections import defaultdict, Counter
from itertools import pairwise
import subprocess


def part1(lines=LINES):
    i = 0
    count = 0
    grid = []
    lst = []
    graph = defaultdict(set)
    text = ''.join(lines)
    # print(text)
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', text)
    for m in matches:
        l,r = m.split(',')
        l = l[l.index('(')+1:]
        r = r [:-1]
        count += int(l) * int(r)
    return count

def part2(lines=LINES):
    i = 0
    count = 0
    grid = []
    lst = []
    graph = defaultdict(set)
    text = ''.join(lines)
    # print(text)
    mult = True
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    dont = r'don\'t\(\)'
    dos = []
    donts = []

    for m in re.finditer(r'do\(\)', text):
        dos.append(m.start())

    for m in re.finditer(r'don\'t\(\)', text):
        donts.append(m.start())
    # print(dos,donts)
    last_do = 0
    last_dont = 0
    for m in re.finditer(pattern, text):
        start_i, end_i, text_m = m.start(), m.end(), m.group()
        l, r = text_m.split(',')
        l = l[l.index('(')+1:]
        r = r[:-1]
        while dos and start_i > dos[0]:
            last_do = dos[0]
            dos.pop(0)

        while donts and start_i > donts[0]:
            last_dont = donts[0]
            donts.pop(0)

        mult = last_do > last_dont
        if last_do == 0 and last_dont == 0:
            mult = True
        if mult:
            count += int(l) * int(r)
            # print(l,r)



    return count



print(f'Part 1 Test Output: {part1(test1)}')
p1_actual = part1(LINES)
subprocess.run("clip", text=True, input=str(p1_actual))
print(f'Part 1 ACTUAL: {p1_actual}   COPIED!')

print(f'Part 2 Test Output: {part2(test1)}')
p2_actual = part2(LINES)
subprocess.run("clip", text=True, input=str(p2_actual))
print(f'Part 2 ACTUAL: {p2_actual}   COPIED!')
