with open('input.txt', 'r') as f:
    LINES = [line[:-1] for line in f.readlines()]
# with open('test1.txt', 'r') as f:
#     test1 = [line[:-1] for line in f.readlines()]


from collections import Counter

def part1(lines=LINES):
    i = 0
    diff = 0
    l1 = []
    l2 = []
    while i < len(lines):
        line = lines[i]
        n, n2 = line.split()
        n = int(n)
        n2 = int(n2)
        l1.append(n)
        l2.append(n2)
        i += 1
    l1.sort()
    l2.sort()

    for n, n2 in zip(l1,l2):
        diff += abs(n-n2)
    return diff


def part2(lines=LINES):
    i = 0
    diff = 0
    l1 = []
    l2 = []
    while i < len(lines):
        line = lines[i]
        n, n2 = line.split()
        n = int(n)
        n2 = int(n2)
        l1.append(n)
        l2.append(n2)
        i += 1

    count = Counter(l2)
    for n in l1:
        diff += n*count[n]
    return diff


print(part1())
print(part2())
